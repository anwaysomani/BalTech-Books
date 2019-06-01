from django import forms
from customer.models import registered_shop

class NewDistributorForm(forms.ModelForm):
    class Meta:
        model = registered_shop
        fields = {'name', 'address', 'district', 'state', 'country', 'pincode', 'employee_id', 'mobile_number',}

        widgets = {
            #'employee_id': forms.TextInput()
        }

        labels = {
            'name': 'Shop Name/POC Name',
            'address': 'Shop Address',
            'mobile_number': 'Mobile Number',
        }

    def __init__(self, *args, **kwargs):
        super(NewDistributorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


