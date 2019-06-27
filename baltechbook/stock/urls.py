from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'inventory/$', views.inventory, name='inventory'),
    url(r'stock-history/$', views.stockHistory, name='stockHistory'),
]
