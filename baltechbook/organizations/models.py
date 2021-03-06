from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from PIL import Image

# Constants
from invoice.constants import STATES, COUNTRIES

# Model for organization information on pages
class organization_table(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    organization_name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=10, blank=True)
    mobileNumber = models.CharField(max_length=10)
    whatsappNumber = models.CharField(max_length=10)
    salesEmail = models.EmailField()
    infoEmail = models.EmailField(null=True)
    logo = models.ImageField(null=True, blank=True)
    addressLine1 = models.CharField(max_length=200)
    addressLine2 = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    pincode = models.IntegerField(validators=[RegexValidator(r'^\d{1,10}$')], null=True)
    branch_office = models.CharField(max_length=100, blank=True, null=True)
    org_code = models.CharField(max_length=3)
    weblink = models.URLField()

    def __str__(self):
        return self.organization_name

    def __unicode__(self):
        return unicode(self.organization_name)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

