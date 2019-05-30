from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import employee_table

# team member view
def team(request, id):
    all_members_list = employee_table.objects.all().order_by('employee_id')

    context = {
        'all_members': all_members_list,
        'id': id,
    }

    return render(request, 'team.html', context)


def team_member(request, id, emp_id):
    member = employee_table.objects.get(employee_id=emp_id)

    context = {
        'member': member,
        'id': id,
    }

    return render(request, 'team-member.html', context)


