from django import forms
from django.forms import ModelForm
from order.models import *


class order_init_details(forms.ModelForm):
    class Meta:
        model = order_table
        fields = {'order_number', 'organization_id'}
        widgets = {
            'order_number': forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
            'organization_id': forms.TextInput(attrs={'class': "form-control", 'readonly': True}),
        }

