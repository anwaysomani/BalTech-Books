from __future__ import unicode_literals
from django.shortcuts import render
from stock.models import products_table

def inventory(request):
    product_list = products_table.objects.all()
    context = {
        'product_list': product_list,
    }

    return render(request, 'inventory.html', context)

def stockHistory(request):
    return render(request, 'stockHistory.html', {})
