from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(products_table)
admin.site.register(stock_table)
admin.site.register(stock_entry_table)
admin.site.register(refill_request_table)
