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
from order.forms import ProductsOrderForm, PaymentForm
from invoice.forms import order_init_details
from customer.forms import ExistingCustomerDetailForm, CustomerBasicDetailForm, ExistingCustomerAddressForm, NewCustomerAddressForm

# Exception Handling
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, EmptyResultSet, ObjectDoesNotExist, ValidationError

# ------------------------------------------------------------------------------
def invoice(request):
    organization = organization_table.objects.all().first()
    organization_id = organization.organization_id

    orders = order_table.objects.all().order_by('-order_id')

    context = {
        'organization_id': organization_id,
        'orders': orders,
    }

    return render(request, 'invoice.html', context)

def orderInitDetails(request):
    user = get_user_model()

    # Extracting organization_code
    organization = organization_table.objects.all().first()
    orgCode = organization.org_code
    orgId = organization.organization_id

    # Extracting order id for new invoice
    order = order_table.objects.all()
    orderId = order.count()+1

    # Extracting employee_id from deferredAttribute
    field_name = 'employee_id'
    obj = get_user_model().objects.first()
    employeeId = getattr(obj, field_name)

    field_email = 'email'
    employee_mail = getattr(obj, field_email)

    # Printing order_number via domain
    order_code = orgCode + str(orgId) + str(employeeId) + "." + str(orderId)

    # Fetch organization id
    field_organization_id = 'organization_id'
    organization_ID = getattr(obj, field_organization_id)

    # Declaring initial data for order form
    initial_data = {
        'order_id': orderId,
        'order_number': order_code,
        'organization_id': orgId,
    }

    # Declaring form for init order details
    form = order_init_details(request.POST or None, initial=initial_data)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('product-order' ,orderId)
        else:
            print(form.errors)
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
        prod_price = form.cleaned_data['product_price']
        new_data.save(prod_id, quant, prod_price)
        form = ProductsOrderForm(request.POST or None, initial=initial_data)

    else:
        form = ProductsOrderForm(request.POST or None, initial=initial_data)

    return render(request, 'selectProducts.html', context)

# Customer Record
def accept_customer_record(request, id):
    customer_records = customer_table.objects.all()
    form_existing = ExistingCustomerDetailForm(request.POST or None)
    form_new = CustomerBasicDetailForm(request.POST)

    context = {
        'id': id,
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
        'id': id,
        'cust_id': cust_id,
        'address_list': address_list,
        'form_existing': form_existing,
        'form_new': form_new,
    }

    if request.method=='POST':
        print("In POST")
        if form_existing.is_valid():
            # Fetch customer id from template
            customerID = form_existing.cleaned_data['customer_address']
            # Fetch customer address matching record
            customer_record = customer_address_table.objects.get(customer_address_id=customerID)
            # Fetch order object
            update_record = order_table.objects.get(order_id=id, customer_id=cust_id)
            # Assign customer_address instance to order table
            update_record.customer_address_id = customer_record
            # Save updated order_table instance
            update_record.save()

            return redirect('order-payment', id)
       

        if form_new.is_valid():
            # Create save instance
            form_new = NewCustomerAddressForm(request.POST)
            # Fake Submission record
            form_submit = form_new.save(commit=False)
            # Update customer_id to fake submission
            form_submit.customer_id = customer_table.objects.get(customer_id=cust_id)
            # Retrieve address from template form data for search render
            customer_address = form_new.cleaned_data['address']
            # Submit new form data(updated)
            form_submit.save()
            # Fetch customer address object from db
            customer_add = customer_address_table.objects.get(address=customer_address)
            # Fetch order object from db
            update_record = order_table.objects.get(order_id=id, customer_id=cust_id)
            # Assign customer_address_id to order table
            update_record.customer_address_id = customer_add
            # Save updated order_table instance
            update_record.save()

            return redirect('order-payment', id)

        else:
            print(form_new.errors)

    return render(request, 'customer-address-record.html', context)


# Order payment
def payment(request, id):
    order_record = order_table.objects.get(order_id=id)
    required_customer_id = order_record.customer_id.customer_id
    required_address_id = order_record.customer_address_id.customer_address_id
    all_products = product_order_table.objects.all().filter(order_id=id)
    customer_info = customer_table.objects.get(customer_id=required_customer_id)
    customer_address = customer_address_table.objects.get(customer_address_id=required_address_id)

    val = 0
    for prod in all_products:
        val = val + prod.product_price

    initial_data = {
        'order_id': id,
        'actual_amount': val,
        'payable_amount': val,
        'discount': 0,
    }

    payment_form = PaymentForm(request.POST or None, initial=initial_data)

    context = {
        'id': id,
        'payment_form': payment_form,
        'order_record': order_record,
        'all_products': all_products,
        'customer_info': customer_info,
        'customer_address': customer_address,
        'val': val,
    }

    if request.method=='POST':
        if payment_form.is_valid():
            sales_exec = payment_form.cleaned_data['sales_executive']
            
            # Fetch order object
            update_record = order_table.objects.get(order_id=id)
            # Assign customer_address instance to order table
            update_record.employee_id = sales_exec
            # Save updated order_table instance
            update_record.save()
            # Save payment form data
            payment_form.save()

            return redirect('final-invoice', id)
        else:
            print(payment_form.errors)

    return render(request, 'orderPayment.html', context)

def generate_invoice(request, id):
    order_record = order_table.objects.get(order_id=id)
    required_customer_id = order_record.customer_id.customer_id
    required_address_id = order_record.customer_address_id.customer_address_id
    all_products = product_order_table.objects.all().filter(order_id=id)
    customer_info = customer_table.objects.get(customer_id=required_customer_id)
    customer_address = customer_address_table.objects.get(customer_address_id=required_address_id)
    payment_record = payment_table.objects.get(order_id=id)

    context = {
        'id': id,
        'order_record': order_record,
        'all_products': all_products,
        'customer_info': customer_info,
        'customer_address': customer_address,
        'payment_record': payment_record,
    }  

    return render(request, 'finalInvoice.html', context)


