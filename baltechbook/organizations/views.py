from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import employee_table
from django.contrib.auth import get_user_model
from organizations.forms import NewDistributorForm

# team member view
def team(request):
    all_members_list = employee_table.objects.filter(employee_type="Administrator").order_by('employee_id')
    all_sales_members_list = employee_table.objects.filter(employee_type="Sales Executive").order_by('city')

    context = {
        'all_members': all_members_list,
        'all_sales_members': all_sales_members_list,
    }

    return render(request, 'team.html', context)


def team_member(request, emp_id):
    member = employee_table.objects.get(employee_id=emp_id)

    context = {
        'member': member,
    }

    return render(request, 'team-member.html', context)

# Sales Executive page for distributor form registration
def distributor_registration(request):
    # Extracting email from deferredAttribute
    field_name = 'id'
    obj = get_user_model().objects.first()
    email = getattr(obj, field_name)

    initial_data = {
        'employee_id': email,
        'state': 'Maharashtra',
        'country': 'India'
    }

    form = NewDistributorForm(request.POST or None, initial=initial_data)
   
    context = {
        'form': form,
    }

    if request.method == "POST":
        if form.is_valid():
            form.save()

    return render(request, 'distributor-registration-form.html', context)

