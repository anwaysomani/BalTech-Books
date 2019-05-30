from __future__ import unicode_literals
from django.shortcuts import render
from customer.models import customer_table, customer_address_table


def customer_record(request):
    customers = customer_table.objects.all()
    
    context = {
        'customers': customers,
    }

    return render(request, 'customer.html', context)

