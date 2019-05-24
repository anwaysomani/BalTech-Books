from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(order_table)
admin.site.register(product_order_table)
admin.site.register(payment_table)
admin.site.register(delivery_record_table)
