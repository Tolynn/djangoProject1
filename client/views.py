import datetime
import os
import requests
from shutil import disk_usage

from rest_framework.response import Response
from rest_framework import viewsets, views, generics
from rest_framework.permissions import IsAdminUser

from .models import User, AvatarImage
from client.serializers import UserSerializer, AvatarSerializer, WeatherSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    """
    Регистрация клиента
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD клиентов
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)


class AvatarImageViewSet(viewsets.ModelViewSet):
    """
    CRUD аватара профиля клиента
    """
    queryset = AvatarImage.objects.all()
    serializer_class = AvatarSerializer


class MemorycheckView(views.APIView):
    """
    Вывод проверки свободного места на сервере
    """

    def get(self, requests):
        dir_app = os.path.abspath(os.curdir).split('\\')[0]
        dir_app += '/'
        result = disk_usage(dir_app)
        gb = 10 ** 9

        return Response(
            {
                'free_memory': f'{round(result.free / gb, 2)} GB',
                'total_memory': f'{round(result.total / gb, 2)} GB',
                'use_memory': f'{round(result.used / gb, 2)} GB',
                'date': datetime.date.today(),
            }
        )


class WeatherSecondView(generics.GenericAPIView):
    """
    Вывод погоды по дате и городу (наименование города транслитом)
    """
    serializer_class = WeatherSerializer

    def post(self, request, *args, **kwargs):
        city = request.data['city']
        date = request.data['date']
        response = requests.get(
            f'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=a0365a415cab41378b0132932230503&q={city}&format=json&date={date}')
        response = response.json()

        city = response['data']['request'][0]['query']
        date = response['data']['weather'][0]['date']
        min_t = response['data']['weather'][0]['mintempC']
        max_t = response['data']['weather'][0]['maxtempC']

        weather = {
            'city': city,
            'date': date,
            'min_temp_C': min_t,
            'max_temp_C': max_t,
        }
        return Response(weather)
