from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from organizations.models import organization_table 
from order.models import *
from order.forms import new_order_for_products
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
    form = new_order_for_products(request.POST, initial_data)

    context = {
        'id': id,
        'form': form,
        'products_list': product_current,
    }
    
    if request.method=='POST':
        form = new_order_for_products(request.POST)
        # Printing all accepted data to see error
        print(request.POST.get('order_id'))
        print(request.POST.get('product_id'))
        print(request.POST.get('quantity'))
        print(request.POST.get('delivery_date'))
        order_id_id = id
        prod_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        val1 = products_table.objects.get(product_id=prod_id)
        form.post_tax_amount = int(val1.post_tax_price) * quantity
        if form.is_valid():
            form.save()
            print("Step 3")
            return redirect('product-order', id)
        else:
            print("Error")

    return render(request, 'selectProducts.html', context)

# Customer Record
def accept_customer_record(request, id):
    return render(request, 'customer-record.html', {})
