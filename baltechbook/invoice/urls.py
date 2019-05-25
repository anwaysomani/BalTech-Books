from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'invoice/$', views.invoice, name='invoice'),
    url(r'invoice/add/$', views.orderInitDetails, name='orderDetails'),
    url(r'invoice/add/selectProducts/(?P<id>\d+)/', views.select_products_for_order, name='product-order'),
    url(r'invoice/add/selectCustomer/(?P<id>\d+)/', views.accept_customer_record, name='customer-records'),
]
