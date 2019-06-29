# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView
from django.urls import reverse
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy

def login(request):
    return render(request, 'registration/login.html', {})

class PanelRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        check = self.request.user.sales_executive
        if check == True:
            return reverse('distributor-form')
        else:
            return reverse('dashboard')

def logout(request):
    return render(request, '', {})
