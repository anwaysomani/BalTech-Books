from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'customer/$', views.customer_record, name='customer-record'),
    url(r'daily-visit-record/$', views.daily_visit_record, name='daily_visit_record'),
]
