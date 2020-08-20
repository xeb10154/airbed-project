from rest_framework import serializers
from main.models import *
import json


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class BookingSerializer(serializers.ModelSerializer):
    # property_name = serializers.SerializerMethodField('propertyName')
    # def propertyName(self, obj):
    #     return obj.property.name

    # User ID who booked into the property has been deliberately omitted.
    # Seen as sensitive info and a security risk.
    class Meta:
        model = Booking
        fields = ('id', 'property', 'review',
                  'startDate', 'endDate', 'cancel')
        read_only_fields = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id',)


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        read_only_fields = ('id',)


class PropertySerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/47258197/django-rest-serializers-return-data-of-related-field
    # https://www.django-rest-framework.org/api-guide/relations/#example
    # bookings = BookingSerializer(many=True, read_only=True)

    media = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    def get_media(self, obj):
        names = obj.media.all().values_list('name', flat=True)
        return names

    def get_img(self, obj):
        return obj.media.all().first().name

    class Meta:
        model = Property
        fields = ('id', 'name', 'beds', 'price', 'roomType', 'address',
                  'location', 'lng', 'lat', 'maxGuests', 'rooms', 'tagline',
                  'info', 'img', 'media')
        read_only_fields = ('id',)


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('id',)
