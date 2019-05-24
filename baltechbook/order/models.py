from __future__ import unicode_literals
from django.db import models
from organizations.models import organization_table
from customer.models import customer_address_table, customer_table
from accounts.models import employee_table
from stock.models import products_table

# Order 
class order_table(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(customer_table)
    organization_id = models.ForeignKey(organization_table)
    customer_address_id = models.ForeignKey(customer_address_table) # Billing address
    customer_address_id = models.ForeignKey(customer_address_table) # Shipping address
    employee_id = models.ForeignKey(employee_table)
    order_number = models.CharField(max_length=9)
    creation_date = models.DateField(auto_now=True)
    creation_time = models.TimeField(auto_now=True)
    status = models.CharField(max_length=11)

    def __unicode__(self):
        return self.order_id

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order's"


# Product orders
class product_order_table(models.Model):
    product_order_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    product_id = models.ForeignKey(products_table)
    quantity = models.IntegerField()
    post_tax_amount = models.DecimalField(max_digits=7, decimal_places=2)
    delivery_date = models.DateField()


# Payment
class payment_table(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    actual_amount = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2)
    payable_amount = models.DecimalField(max_digits=5, decimal_places=2)
    mode_of_payment = models.CharField(max_length=7)


# Order Delivery Records
class delivery_record_table(models.Model):
    delivery_record_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(order_table)
    delivery_date = models.DateField()
    actual_delivery_date = models.DateField()

