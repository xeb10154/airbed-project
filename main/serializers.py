from rest_framework import serializers
from main.models import *


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # class Meta:
    #     model = Booking
    #     fields = '__all__'

    # class Meta:
    #     model = Property
    #     fields = '__all__'
