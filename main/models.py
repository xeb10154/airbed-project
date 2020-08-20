import datetime

from django.db import models


class Location(models.Model):

    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    imgUrl = models.CharField(max_length=255, null=True)
    experiences = models.ForeignKey(
        'Experience', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.city


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    property = models.ForeignKey(
        'Property', related_name='media', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    # An addtional one-to-many field for user -> property should be
    # added to show ownership of the property created by a user.
    # For simplicity this was omitted.
    name = models.CharField(max_length=100)
    beds = models.IntegerField(blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    roomType = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, null=True)
    lng = models.DecimalField(decimal_places=2, max_digits=6)
    lat = models.DecimalField(decimal_places=2, max_digits=6)
    maxGuests = models.IntegerField(blank=False)
    rooms = models.IntegerField(blank=False)
    tagline = models.CharField(max_length=500)
    info = models.CharField(max_length=1000, null=True)
    img = models.ForeignKey(
        'Gallery', related_name='thumbnail', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    score = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.score}'


class Review(models.Model):
    rating = models.ForeignKey(
        'Rating', related_name='reviews', on_delete=models.CASCADE)
    user = models.CharField(max_length=128)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.description


class Booking(models.Model):
    user = models.ForeignKey(
        'User', related_name='bookings', on_delete=models.SET_NULL, null=True)
    property = models.ForeignKey(
        'Property', related_name='bookings', on_delete=models.SET_NULL, null=True)
    review = models.ForeignKey(
        'Review', related_name='bookings', on_delete=models.CASCADE, null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.property.name} - {self.user.firstName}"


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
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    imgUrl = models.CharField(max_length=500)

    def __str__(self):
        return self.title
