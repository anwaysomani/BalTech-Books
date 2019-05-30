from __future__ import unicode_literals
from django.shortcuts import render
from customer.models import customer_table, customer_address_table


def customer_record(request):
    
    context = {
    }

    return render(request, 'customer.html', context)

