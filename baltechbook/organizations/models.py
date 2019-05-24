from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from PIL import Image

# Model for organization information on pages
class organization_table(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    organization_name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    mobileNumber = models.CharField(max_length=10)
    whatsappNumber = models.CharField(max_length=10)
    salesEmail = models.EmailField()
    infoEmail = models.EmailField(null=True)
    logo = models.ImageField(null=True)
    addressLine1 = models.CharField(max_length=200)
    addressLine2 = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')], null=True)

