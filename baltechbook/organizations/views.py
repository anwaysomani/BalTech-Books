from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import employee_table

# team member view
def team(request):
    all_members_list = employee_table.objects.all().order_by('employee_id')
    all_sales_members_list = employee_table.objects.filter(employee_type="Sales Executive")

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


