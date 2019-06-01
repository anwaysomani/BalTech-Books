from __future__ import unicode_literals
from django.db import models
from customer.models import customer_table
from invoice.constants import GST_RATE, REFILL_REQUEST_TYPE

# Product list table
class products_table(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    actual_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cgst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE, default=0)
    sgst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE, default=0)
    igst_tax = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, choices=GST_RATE, default=0)
    post_tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    launch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.actual_price > 0:
            # Assign check values to variable
            cgst = 0
            sgst = 0
            igst = 0
            
            # Fetching proportion value
            if self.cgst_tax > 0:
                cgst = self.cgst_tax/100
            if self.sgst_tax > 0:
                sgst = self.sgst_tax/100
            if self.igst_tax > 0:
                igst = self.igst_tax/100

            # Calculating value for gst's
            cgst_value = self.actual_price * cgst
            sgst_value = self.actual_price * sgst
            igst_value = self.actual_price * igst

            # Assigning value for post_tax_amount
            self.post_tax_price = self.actual_price + cgst_value + sgst_value + igst_value

        # Calling save method
        super(products_table, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

# Stock Records
class stock_table(models.Model):
    stock_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    total_production_quantity = models.IntegerField()
    current_quantity = models.IntegerField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

# New Stock Entry
class stock_entry_table(models.Model):
    stock_entry_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    refill_quantity = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stock Entry"
        verbose_name_plural = "Stock Entries"

# Refill Request for Stock
class refill_request_table(models.Model):
    refill_request_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(products_table)
    customer_id = models.ForeignKey(customer_table, null=True, blank=True)
    request_quantity = models.IntegerField()
    request_date = models.DateTimeField(auto_now=True)
    request_status = models.CharField(max_length=10, choices=REFILL_REQUEST_TYPE)

    class Meta:
        verbose_name = "Refill Request"
        verbose_name_plural = "Refill Requests"

