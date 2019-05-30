from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'customer/$', views.customer_record, name='customer-record'),
]
