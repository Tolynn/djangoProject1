from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (('F', ('Female')), ('M', ('Male')),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class AvatarImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar' )
    avatar = models.ImageField(upload_to='images/', null=True, max_length=255)




# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile' )
#     def __str__(self):
#         return self.product.title
