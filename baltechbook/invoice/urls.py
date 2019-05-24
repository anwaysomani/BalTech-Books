from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'invoice/$', views.invoice, name='invoice'),
    url(r'invoice/add/$', views.newInvoice, name='new-invoice'),
]
