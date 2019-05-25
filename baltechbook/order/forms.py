from django import forms
from django.forms import ModelForm
from .models import *


class new_order_for_products(forms.ModelForm):
    class Meta:
        model = product_order_table
        fields = {'product_id', 'quantity', 'delivery_date'}
        widgets = {
            'product_id': forms.TextInput(),
            'delivery_date': forms.DateInput(format='%d%m%y')
        }

