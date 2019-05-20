from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Administrators(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Accounters(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


#class Organization(models.Model):
#    organization_name = models.CharField(max_length=150)
#    organization_dol = models.DateField()

