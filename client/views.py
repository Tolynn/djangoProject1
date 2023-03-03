from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import User, AvatarImage
from django.shortcuts import render
from rest_framework import viewsets, views, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from client.serializers import UserSerializer, AvatarSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = AvatarImage.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = (IsAuthenticated,)


