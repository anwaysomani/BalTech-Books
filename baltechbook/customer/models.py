from __future__ import unicode_literals
from django.db import models
from invoice.constants import STATES, COUNTRIES, ADDRESS_TYPE

# Customer Record
class customer_table(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    mobileNumber = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name + " | " + self.email

    def __str__(self):
        return self.name

# Customer Address
class customer_address_table(models.Model):
    customer_address_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(customer_table, default=1)
    address_type = models.CharField(max_length=9, choices=ADDRESS_TYPE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    state = models.CharField(max_length=35, choices=STATES)
    country = models.CharField(max_length=50, choices=COUNTRIES)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)

