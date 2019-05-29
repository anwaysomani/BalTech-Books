from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# Redirect
from django.http import HttpResponseRedirect

# Messaging framework
from django.contrib import messages

# Importing models
from organizations.models import organization_table 
from order.models import *
from stock.models import products_table

# Importing forms
from order.forms import ProductsOrderForm
from invoice.forms import order_init_details
from customer.forms import ExistingCustomerDetailForm, CustomerBasicDetailForm, ExistingCustomerAddressForm, NewCustomerAddressForm

# Exception Handling
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, EmptyResultSet, ObjectDoesNotExist, ValidationError

# ------------------------------------------------------------------------------
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
        'order_id': id,
    }
    form = ProductsOrderForm(request.POST or None, initial=initial_data)

    context = {
        'id': id,
        'form': form,
        'products_list': product_current,
    }
    
    if request.method=='POST' and form.is_valid():
        form = ProductsOrderForm(request.POST)
        new_data = form.save(commit=False)
        prod_id = form.cleaned_data['product_id']
        quant = form.cleaned_data['quantity']

        #print(new_data.order_id)
        #new_data.order_id = id
             
        new_data.save(prod_id, quant)

    else:
        form = ProductsOrderForm(request.POST or None, initial=initial_data)

    return render(request, 'selectProducts.html', context)

# Customer Record
def accept_customer_record(request, id):
    customer_records = customer_table.objects.all()
    form_existing = ExistingCustomerDetailForm(request.POST or None)
    form_new = CustomerBasicDetailForm(request.POST)

    context = {
        'list': customer_records,
        'form_existing': form_existing,
        'form_new': form_new,
    }

    if request.method=='POST': 
        update_record = order_table.objects.get(order_id=id)
        if form_existing.is_valid():
            cust_id = form_existing.cleaned_data['customer_info']
            update_record.customer_id = customer_table.objects.get(customer_id=cust_id)
            update_record.save()
            return redirect('customer-address', id, cust_id)

        elif form_new.is_valid():
            c_name = form_new.cleaned_data['name']
            c_emailAddress = form_new.cleaned_data['email']
            c_number = form_new.cleaned_data['mobileNumber']
            try:
                n = customer_table.objects.get(name=c_name, email=c_emailAddress, mobileNumber=c_number)
            except EmptyResultSet:
                return HttpResponseRedirect(self.request.path_info)
                form_new.save() 

                try:
                    cusid = customer_table.objects.get(name=c_name, email=c_emailAddress, mobileNumber=c_number)
                    update_record.customer_id  = cusid
                    cust_id = update_record.customer_id
                    update_record.save()
                    return redirect('customer-address', id, cust_id)
                
                except MultipleObjectsReturned:
                    return HttpResponseRedirect(self.request.path_info)
                    messages.error(request, "Seems the customer already exists...Please select data from below list!")

            except ObjectDoesNotExist:
                form_new.save()

                try:
                    cusid = customer_table.objects.get(name=c_name, email=c_emailAddress, mobileNumber=c_number)
                    update_record.customer_id = cusid
                    cust_id = cusid.customer_id
                    update_record.save()
                    return redirect('customer-address', id, cust_id)

                except MultipleObjectsReturned:
                    return HttpResponseRedirect(self.request.path_info)
                    messages.error(request, "Seems the customer already exists...Please select customer from below list!")

            except MultipleObjectsReturned:
                return HttpResponseRedirect(self.request.path_info)
                messages.error(request, "Customer already exists")

    return render(request, 'customer-record.html', context)

# Customer address
def accept_customer_address(request, id, cust_id):
    address_list = customer_address_table.objects.filter(customer_id=cust_id)

    initial_data = {
        'customer_id': cust_id,
    }

    form_existing = ExistingCustomerAddressForm(request.POST)
    form_new = NewCustomerAddressForm(request.POST or None, initial=initial_data)

    context = {
        'address_list': address_list,
        'form_existing': form_existing,
        'form_new': form_new,
    }

    if request.method=='POST':
        print("In POST")
        if form_existing.is_valid():
            print("Here Again!")
       

        if form_new.is_valid():
            form_new = NewCustomerAddressForm(request.POST)
            form_submit = form_new.save(commit=False)

            #customer_id = form_submit.cleaned_data['customer_id']
            form_submit.customer_id = customer_table.objects.get(customer_id=cust_id)
            customer_address = form_new.cleaned_data['address']
            form_submit.save()
            customer_add = customer_address_table.objects.get(address=customer_address)
            update_record = order_table.objects.get(order_id=id, customer_id=cust_id)
            update_record.customer_address_id = customer_add
            update_record.save()

        else:
            print(form_new.errors)

    return render(request, 'customer-address-record.html', context)

