from __future__ import unicode_literals
from django.db import models
from customer.models import customer_table
from invoice.constants import GST_RATE, REFILL_REQUEST_TYPE

# Product list table
class products_table(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    actual_price = models.DecimalField(max_digits=7, decimal_places=2)
    cgst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE)
    sgst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE)
    igst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE)
    post_tax_price = models.DecimalField(max_digits=7, decimal_places=2)
    launch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


# Stock Records
class stock_table(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    total_production_quantity = models.IntegerField()
    current_quantity = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)


# New Stock Entry
class stock_entry_table(models.Model):
    stock_entry_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    refill_quantity = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)


# Refill Request for Stock
class refill_request_table(models.Model):
    refill_request_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    customer_id = models.ForeignKey(customer_table, null=True, blank=True)
    request_quantity = models.IntegerField()
    request_date = models.DateTimeField(auto_now=True)
    request_status = models.CharField(max_length=10, choices=REFILL_REQUEST_TYPE)

