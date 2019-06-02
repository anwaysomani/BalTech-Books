from __future__ import unicode_literals
from django.db import models
from invoice.constants import STATES, COUNTRIES, ADDRESS_TYPE
from django.core.validators import RegexValidator
from accounts.models import employee_table

# Customer Record
class customer_table(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True, blank=True)
    mobileNumber = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name + " | " + self.email

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

# Customer Address
class customer_address_table(models.Model):
    customer_address_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(customer_table, default=1)
    address_type = models.CharField(max_length=9, choices=ADDRESS_TYPE)
    address = models.CharField(max_length=200, unique=True)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    state = models.CharField(max_length=35, choices=STATES, default='Maharashtra')
    country = models.CharField(max_length=50, choices=COUNTRIES, default='India')
    phoneNumber = models.CharField(max_length=10, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Customer's Address"
        verbose_name_plural = "Customers Addresses"

# Model for Sales Executive
class registered_shop(models.Model):
    shop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATES)
    country = models.CharField(max_length=100, choices=COUNTRIES)
    pincode = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')], null=True)
    employee_id = models.ForeignKey(employee_table, null=True)

    
