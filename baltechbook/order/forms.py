from django import forms
from .models import *
from stock.models import products_table
from invoice.constants import *

class ProductsOrderForm(forms.ModelForm):
    class Meta:
        model = product_order_table
        fields = {'order_id', 'product_id', 'quantity', 'delivery_date', 'product_price'}

        widgets = {
            'order_id': forms.TextInput(attrs={'readonly': True})
        }

        labels = {
            'product_id': 'Select a Product',
            'quantity': 'Enter Supply Quantity',
            'product_price': 'Enter Product Price',
            'delivery_date': 'Enter Delivery Date',
            'order_id': 'Order ID'
        }

    def __init__(self, *args, **kwargs):
        super(ProductsOrderForm, self).__init__(*args, **kwargs)
        self.fields['product_id'].queryset = products_table.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'delivery_date':
                field.widget.attrs['placeholder'] = 'Enter in the following format YYYY-MM-DD'
            elif field_name == 'quantity':
                field.widget.attrs['placeholder'] = 'Enter a number'


# Payment form
class PaymentForm(forms.ModelForm):
    sales_executive = forms.ModelChoiceField(employee_table.objects.none(), required=False)

    class Meta:
        model = payment_table
        fields = {'order_id', 'actual_amount', 'discount', 'payable_amount', 'mode_of_payment'}

        widgets = {
            'order_id': forms.Select(attrs={'readonly': True}),
            'actual_amount': forms.TextInput(attrs={'readonly': True}),
            'payable_amount': forms.TextInput(attrs={'readonly': True})
        }

        labels = {
            'employee_id': 'Reference',
        }

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['sales_executive'].queryset = employee_table.objects.filter(employee_type="Sales Executive")
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        return super(PaymentForm, self).save(commit=commit)
