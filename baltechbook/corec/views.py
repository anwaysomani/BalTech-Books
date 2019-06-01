from __future__ import unicode_literals
from django.shortcuts import render
from accounts.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = get_user_model()

    organization = organization_table.objects.all().first()
    id = organization.organization_id

    context = {
        'id': id,
        user : 'user',
    }
    return render(request, 'dashboard.html', context)

def blank(request):
    return render(request, 'blank.html', context)


# Error Pages
# Error: 403
def error_403(request):
    return render(request, 'errors/403.html', {})

# Error: 404
def error_404(request):
    return render(request, 'errors/404.html', {})

# Error: 500
def error_500(request):
    return render(request, 'errors/500.html', {})

