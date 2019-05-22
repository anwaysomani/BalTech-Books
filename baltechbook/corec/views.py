from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import *
from .forms import UserForm

def dashboard(request):
    user = request.user
    context = {
        user : 'user',
    }
    return render(request, 'dashboard.html', context)

def invoice(request):
    return render(request, 'invoice.html', {})

def blank(request):
    form = UserForm()
    users = User.objects.all()
    context = {
        'form': form,
        'users': users,
    }
    
    if request.method == "POST":
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'blank.html', context)

