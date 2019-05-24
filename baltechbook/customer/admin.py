from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(customer_table)
admin.site.register(customer_address_table)
