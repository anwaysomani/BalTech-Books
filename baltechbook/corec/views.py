from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import *
from django.contrib.auth import get_user_model
#from .forms import UserForm

def dashboard(request):
    user = get_user_model()
    context = {
        user : 'user',
    }
    return render(request, 'dashboard.html', context)

def blank(request):
    return render(request, 'blank.html', context)

