from .models import User
from django.shortcuts import render
from rest_framework import viewsets

from client.serializers import UserSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer