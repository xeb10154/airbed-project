from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json
from datetimerange import DateTimeRange
from rest_framework import generics
from main.models import *
from main.serializers import (UserSerializer,
                              PropertySerializer,
                              BookingSerializer)


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


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
        user = User.objects.get(pk=1)
    except (KeyError, Choice.DoesNotExist):
        return HttpResponseNotFound("You need to be logged in to book a property.")
    else:
        booking = Booking.objects.create(
            user=user, property=property, startDate=startDate, endDate=endDate)
        booking.save()
        return HttpResponse(f'Booking for {property} is successful')
