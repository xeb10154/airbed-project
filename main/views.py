from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.db.models import Q

import requests
import json

from datetimerange import DateTimeRange
from datetime import datetime
from rest_framework import generics, viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from main.models import *
from main.serializers import (UserSerializer,
                              PropertySerializer,
                              BookingSerializer,
                              ExperienceSerializer,
                              LocationSerializer,
                              ReviewSerializer,
                              GallerySerializer)


class SetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)


class ReviewViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset

        propId = self.request.query_params.get('property')

        if not propId:
            return Response(
                data={"error": "Key 'property' not found in request query params"},
                status=status.HTTP_400_BAD_REQUEST)

        queryset = queryset.filter(Q(bookings__property=propId))

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)


class PropertyViewSet(viewsets.ModelViewSet):
    # This is the property list view when user is not logged in
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    pagination_class = SetPagination

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    # def get_ids(obs):
    #     """Get ids from an array of objects"""
    #     return obs.id

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        locations = self.request.query_params.get('location')
        startDate = self.request.data.get('startDate')
        endDate = self.request.data.get('endDate')

        queryset = self.queryset
        if locations:
            location_ids = self._params_to_ints(locations)
            queryset = queryset.filter(location__id__in=location_ids)
        if startDate and endDate:
            startA = datetime.datetime.strptime(
                startDate, '%Y-%m-%dT%H:%M:%S.%f%z')
            endA = datetime.datetime.strptime(
                endDate, '%Y-%m-%dT%H:%M:%S.%f%z')
            queryset = queryset.filter(
                Q(bookings__startDate__gt=endA) |
                Q(bookings__endDate__lt=startA))

        return queryset

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)

    # def perform_create(self, serializer):

    #     # The POST request will come with JSON payload of number, street, city and postcode
    #     formData = self.request.data
    #     number = formData.get('number')
    #     street = formData.get('street')
    #     city = formData.get('city')

    #     res = requests.get(
    #         f'https://maps.googleapis.com/maps/api/geocode/json?address={number} {street},+{city}&key={settings.GEOCODING_API_KEY}')

    #     resData = res.json()['results'][0]

    #     # response body contains geocoding data
    #     geoAddress = resData['formatted_address']
    #     geoData = resData['address_components']
    #     lat = resData['geometry']['location']['lat']
    #     lng = resData['geometry']['location']['lng']
    #     geoCity = geoData[2]['long_name']
    #     geoCountry = geoData[5]['long_name']

    #     locationExists = Location.objects.filter(city=geoCity).exists()
    #     if not locationExists:
    #         Location.objects.create(city=geoCity, country=geoCountry)

    #     location = Location.objects.get(city=geoCity)

    #     serializer.save(location=location,
    #                     address=geoAddress,
    #                     lat=lat,
    #                     lng=lng)


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery
    serializer_class = GallerySerializer

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        # Logic to be added to return an array of existing bookings
        # on a selected property (array of date ranges)

        # Add it here or use .list()?

        # The user id is hardcoded to be 1 since no login system exist
        # Returned bookings are not cancelled.
        return self.queryset.filter(user_id=1, cancel=False)

    def create(self, request, *args, **kwargs):
        u = {'user': 1}
        data = request.data
        data.update(u)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Get submitted dates and property id
        startDate = self.request.data.get('startDate')
        endDate = self.request.data.get('endDate')
        propId = self.request.data.get('property')

        # retrieve list of bookings for this property
        bookingsList = self.queryset.filter(property_id=propId)
        # Create date range from request
        inserted_range = DateTimeRange(startDate, endDate)

        # Compare ranges for booking overlaps
        for booking in bookingsList:
            booking_range = DateTimeRange(booking.startDate, booking.endDate)
            if inserted_range.is_intersection(booking_range):
                return Response(
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)


class GetAllBookingsForPropertyID(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset

        propId = self.request.query_params.get('property')

        if not propId:
            return Response(
                data={"error": "Key 'property' not found in request query params"},
                status=status.HTTP_400_BAD_REQUEST)

        queryset = queryset.filter(Q(property__id=propId) & Q(cancel=False))

        serializer = BookingSerializer(queryset, many=True)
        return Response(serializer.data)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def destroy(self, request, pk=None):
        # Overriding the destroy method to stop delete requests through the API
        return Response(status=status.HTTP_403_FORBIDDEN)
