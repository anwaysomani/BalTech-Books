from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from PIL import Image

# Model for organization information on pages
class organization(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    country = models.CharField(max_length=75)
    contactNumber = models.IntegerField()
    emailAddress = models.EmailField(max_length=200)
    webLink = models.URLField()
    gstNo = models.CharField(max_length=15)
    authorizedGeneral = models.CharField(max_length=100)
    organizationLogo = models.ImageField()
    totalOfficials = models.IntegerField()

    def __str__(self):
        return self.name

