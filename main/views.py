from main.models import *
from main.serializers import MainSerializer
from rest_framework import generics


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = MainSerializer
