from django.db import models
from django.contrib.auth.models import User
# from .manager import *
# Create your models here.


class Customerprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13, null=True, unique=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=20)
    division = models.CharField(max_length=20, help_text='Country/State')
    zip = models.CharField(max_length=10)