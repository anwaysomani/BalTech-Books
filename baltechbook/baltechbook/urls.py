"""baltechbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from corec import views as corviews
from corec.views import error_403, error_404, error_500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', include('accounts.urls')), 
    url('', include('corec.urls')),
    url('', include('customer.urls')),
    url('', include('dev.urls')),
    url('', include('invoice.urls')),
    url('', include('order.urls')),
    url('', include('organizations.urls')),
    url('', include('stock.urls')),
]

handler403 = corviews.error_403 
handler404 = corviews.error_404
handler500 = corviews.error_500
