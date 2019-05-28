from __future__ import unicode_literals
from django.db import models
from organizations.models import organization_table
from customer.models import customer_address_table, customer_table
from accounts.models import employee_table
from stock.models import products_table

# Constants
from invoice.constants import MODE_OF_PAYMENT, ORDER_STATUS, QUANTITY

# Order 
class order_table(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customer_table, blank=True, null=True)
    organization_id = models.ForeignKey(organization_table, null=True, blank=True, default="")
    customer_address_id = models.ForeignKey(customer_address_table, null=True, blank=True, default="") # Billing/Shipping address
    employee_id = models.ForeignKey(employee_table, null=True, blank=True, default="")
    order_number = models.CharField(max_length=11)
    creation_date = models.DateField(auto_now=True, null=True)
    creation_time = models.TimeField(auto_now=True, null=True)
    status = models.CharField(max_length=11, null=True, default="", choices=ORDER_STATUS)

    def __unicode__(self):
        val = str(self.order_id)
        return val

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        #unique_together  = (("order_id", "order_number"))


# Product orders
class product_order_table(models.Model):
    product_order_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    product_id = models.ForeignKey(products_table)
    quantity = models.IntegerField()
    post_tax_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    delivery_date = models.CharField(max_length=10, default="", null=True, blank=True)

    def save(self, prod_name, quant, *args, **kwargs):
        to_read = products_table.objects.values_list('post_tax_price', flat=True).get(name=prod_name)
        value = to_read
        self.post_tax_amount = value * quant
        super(product_order_table, self).save(*args, **kwargs)

# Payment
class payment_table(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    actual_amount = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    payable_amount = models.DecimalField(max_digits=5, decimal_places=2)
    mode_of_payment = models.CharField(max_length=7, choices=MODE_OF_PAYMENT)


# Order Delivery Records
class delivery_record_table(models.Model):
    delivery_record_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    delivery_date = models.DateField()
    actual_delivery_date = models.DateField()

