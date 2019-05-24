from __future__ import unicode_literals
from django.shortcuts import render

def invoice(request):
    return render(request, 'invoice.html', {})


def newInvoice(request):
    return render(request, 'newInvoice.html', {})
