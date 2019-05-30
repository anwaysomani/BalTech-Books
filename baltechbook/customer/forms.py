from django import forms
from .models import customer_table, customer_address_table

class CustomerBasicDetailForm(forms.ModelForm):
    class Meta:
        model = customer_table
        fields = {'name', 'mobileNumber', 'email'}

        labels = {
            'name': "Customer's Name",
            'email': "Customer's Email Address",
            'mobileNumber': "Customer's Mobile Number"
        }

    def __init__(self, *args, **kwargs):
        super(CustomerBasicDetailForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ExistingCustomerDetailForm(forms.Form):
    customer_info = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ExistingCustomerDetailForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['readonly'] = True
            visible.field.widget.attrs['placeholder']  = "Select a Customer from below list and if found, click on the name and then press 'Found the Customer' button"

# ----------------
# Customer Address

class NewCustomerAddressForm(forms.ModelForm):
    class Meta:
        model = customer_address_table
        fields = {'address', 'city', 'state', 'country', 'pincode', 'phoneNumber', 'email', 'address_type', 'customer_id'}

        widgets = {
            'customer_id': forms.TextInput(attrs={'readonly': True})
        }

        labels = {
                'phoneNumber': 'Alternate Mobile Number',
                'email': 'Alternate Email Address',
        }

    def __init__(self, *args, **kwargs):
        super(NewCustomerAddressForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ExistingCustomerAddressForm(forms.Form):
    customer_address = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(ExistingCustomerAddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['readonly'] = True
            visible.field.widget.attrs['placeholder']  = "Select a Customer Address from below list and if found, click on the address and then press 'Proceed to Payment' button" 
