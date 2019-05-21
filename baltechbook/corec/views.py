from __future__ import unicode_literals
from django.shortcuts import render

def dashboard(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)

def invoice(request):
    return render(request, 'invoice.html', {})
