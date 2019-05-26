from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from organizations.models import organization_table 
from order.models import *
from order.forms import ProductsOrderForm
from invoice.forms import order_init_details
from stock.models import products_table

def invoice(request):
    return render(request, 'invoice.html', {})


#def newInvoice(request):
#    return render(request, 'newInvoice.html', {})


def orderInitDetails(request):
    user = get_user_model()

    # Extracting organization_code
    organization = organization_table.objects.get(organization_id=1)
    orgCode = organization.org_code
    orgId = organization.organization_id

    # Extracting order id for new invoice
    order = order_table.objects.all()
    orderId = order.count()+1

    # Extracting employee_id from deferredAttribute
    field_name = 'employee_id'
    obj = get_user_model().objects.first()
    employeeId = getattr(obj, field_name)

    # Printing order_number via domain
    order_code = orgCode + str(orgId) + str(employeeId) + "." + str(orderId)

    # Declaring initial data for order form
    initial_data = {
        'order_id': orderId,
        'order_number': order_code
    }

    # Declaring form for init order details
    form = order_init_details(request.POST or None, initial=initial_data)

    if form.is_valid():
        form.save()
        return redirect('product-order' ,orderId)
    else:
        form = order_init_details(initial=initial_data)

    context = {
        'orderId': orderId,
        'order_code': order_code,
        'form': form,
    }
    
    return render(request, 'initialOrderDetails.html', context)

# Selecting products
def select_products_for_order(request, id):
    product_current = product_order_table.objects.filter(order_id_id=id)
    initial_data = {
        'order_id': id
    }
    form = ProductsOrderForm(request.POST, initial_data)

    context = {
        'id': id,
        'form': form,
        'products_list': product_current,
    }
    
    if request.method=='POST':
        form = ProductsOrderForm(request.POST)
        new_data = form.save(commit=False)

        if form.is_valid():
            print("Entered in the validation")
            order_id = form.cleaned_data['order_id']
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            delivery_date = form.cleaned_data['delivery_date']
             
            new_data.save(product_id)

    else:
        form = ProductsOrderForm(request.POST, initial_data)

    return render(request, 'selectProducts.html', context)

# Customer Record
def accept_customer_record(request, id):
    return render(request, 'customer-record.html', {})
