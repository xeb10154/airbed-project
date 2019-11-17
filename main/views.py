from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.conf import settings

import requests
import json
from datetimerange import DateTimeRange
from rest_framework import generics, viewsets
from main.models import *
from main.serializers import (UserSerializer,
                              PropertySerializer,
                              BookingSerializer,
                              ExperienceSerializer,
                              LocationSerializer)


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PropertyListCreate(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):

        # The POST request will come with JSON payload of number, street, city and postcode
        formData = self.request.data
        number = formData['number']
        street = formData['street']
        city = formData['city']

        res = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={number} {street},+{city}&key={settings.GEOCODING_API_KEY}')

        resData = res.json()['results'][0]

        # response body contains geocoding data
        geoAddress = resData['formatted_address']
        geoData = resData['address_components']
        lat = resData['geometry']['location']['lat']
        lng = resData['geometry']['location']['lng']
        geoCity = geoData[2]['long_name']
        geoCountry = geoData[5]['long_name']

        locationExists = Location.objects.filter(city=geoCity).exists()
        if not locationExists:
            Location.objects.create(city=geoCity, country=geoCountry)

        location = Location.objects.get(city=geoCity)

        serializer.save(location=location,
                        address=geoAddress,
                        lat=lat,
                        lng=lng)


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ExperienceListCreate(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # return JsonResponse({'locationData': [
    #     'Glasgow', 'Edinburgh', 'Stirling'
    # ]
    # })


@csrf_exempt
def book(request, property_id):

    property = get_object_or_404(Property, pk=property_id)
    body = json.loads(request.body)
    startDate = body['startDate']
    endDate = body['endDate']

    bookingsList = Booking.objects.filter(property_id=1)

    inserted_range = DateTimeRange(startDate, endDate)

    # create range object and compare
    for booking in bookingsList:
        booking_range = DateTimeRange(booking.startDate, booking.endDate)
        if inserted_range.is_intersection(booking_range):
            return HttpResponse('This date range is already booked!')

    try:
        # Check current user id is not null and assign value
        # User.logged_in != None
        # This will eventually need to get_model_user() ID from current logged in user
        # Currently hardcoded.
        user = User.objects.get(pk=1)
    except (KeyError, Choice.DoesNotExist):
        return HttpResponseNotFound("You need to be logged in to book a property.")
    else:
        booking = Booking.objects.create(
            user=user, property=property, startDate=startDate, endDate=endDate)
        booking.save()
        return HttpResponse(f'Booking for {property} is successful')
