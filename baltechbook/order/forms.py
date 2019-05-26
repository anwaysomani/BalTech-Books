from django import forms
from .models import *
from stock.models import products_table
from invoice.constants import *

class ProductsOrderForm(forms.ModelForm):
    class Meta:
        model = product_order_table
        fields = {'order_id', 'product_id', 'quantity', 'delivery_date'}
    
        labels = {
            'product_id': 'Select Product'
        }

    def __init__(self, *args, **kwargs):
        super(ProductsOrderForm, self).__init__(*args, **kwargs)
        self.fields['product_id'].queryset = products_table.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


