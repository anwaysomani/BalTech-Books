from __future__ import unicode_literals
from django.db import models

# Customer Record
class customer_table(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

# Customer Address
class customer_address_table(models.Model):
    customer_address_id = models.IntegerField(primary_key=True)
    address_type = models.CharField(max_length=9)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    state = models.CharField(max_length=35)
    country = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)

