from __future__ import unicode_literals
from django.shortcuts import render
from customer.models import customer_table, customer_address_table, registered_shop


def customer_record(request):
    customers = customer_table.objects.all()
    
    context = {
        'customers': customers,
    }

    return render(request, 'customer.html', context)

def daily_visit_record(request):
    shops = registered_shop.objects.all()
    context = {
        'shops': shops,
    }

    return render(request, 'daily_visit_record.html', context)
