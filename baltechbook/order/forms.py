from django import forms
from .models import *
from stock.models import products_table
from invoice.constants import *

class new_order_for_products(forms.ModelForm):
    class Meta:
        model = product_order_table
        fields = {'order_id', 'product_id', 'quantity', 'delivery_date'}
        widgets = {
            'order_id': forms.HiddenInput()
        }
        #widgets = {
        #    'product_id': forms.Select(attrs={'class': "form-control"}),
        #    'quantity': forms.NumberInput(attrs={'class': "form-control"}),
        #    'delivery_date': forms.TextInput(attrs={'class': "form-control"})
        #}

        labels = {
            'product_id': 'Select Product'
        }

    def __init__(self, id, *args, **kwargs):
        super(new_order_for_products, self).__init__(*args, **kwargs)
        self.fields['product_id'].queryset = products_table.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

