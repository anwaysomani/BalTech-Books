from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import get_user_model
from organizations.models import organization_table 
from order.models import *

def invoice(request):
    return render(request, 'invoice.html', {})


def newInvoice(request):
    return render(request, 'newInvoice.html', {})


def orderInitDetails(request):
    user = get_user_model()
    organization = organization_table.objects.get(organization_id=1)
    order = order_table.objects.all()

    orgCode = organization.org_code
    orgId = organization.organization_id
    employeeId = get_user_model()
    employeeActual = employeeId.employee_id
    orderId = order.count()+1

    order_code = orgCode + " " + str(orgId) + " " + str(orderId)

    context = {
        'orderId': orderId,
        'order_code': order_code,
    }
    
    return render(request, 'initialOrderDetails.html', context)

