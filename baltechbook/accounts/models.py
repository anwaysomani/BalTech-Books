from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from organizations.models import organization
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import *

# Contstants: userType, city, state, country
class User(AbstractUser):
    employee_id = models.CharField(max_length=5, null=True)
    organization = models.CharField(max_length=32, null=True)
    contactNum = models.CharField(max_length=10, null=True)
    userType = models.CharField(max_length=15, choices=USERTYPE, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=40, null=True)
    state = models.CharField(max_length=30, choices=STATES, null=True)
    country = models.CharField(max_length=35, choices=COUNTRY, null=True)
    pincode = models.CharField(max_length=6, null=True)



