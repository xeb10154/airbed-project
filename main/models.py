import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Property(models.Model):

    name = models.CharField(max_length=100)
    beds = models.IntegerField(blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    roomType = models.CharField(max_length=100)
    rating = models.IntegerField()
    address = models.CharField(max_length=100)
    lng = models.DecimalField(decimal_places=2, max_digits=6)
    lat = models.DecimalField(decimal_places=2, max_digits=6)
    maxGuests = models.IntegerField(blank=False)
    rooms = models.IntegerField(blank=False)
    details = models.CharField(max_length=500)
    imgUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Booking(models.Model):

    user = models.ForeignKey(
        'User', related_name='bookings', on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey(
        'Property', related_name='bookings', on_delete=models.SET_NULL, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()


class User(models.Model):

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    properties = models.ManyToManyField(
        'Property', through='Booking', related_name='properties')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Experience(models.Model):

    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    imgUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.title
