from django.contrib.auth.hashers import make_password

from .models import User, AvatarImage
from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    date=serializers.DateField()
    city=serializers.CharField(max_length=255)
class AvatarSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = AvatarImage
        fields = ('user','avatar')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password', 'gender', 'birth_date']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)