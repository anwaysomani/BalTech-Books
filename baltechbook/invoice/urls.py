from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'invoice/$', views.invoice, name='invoice'),
    url(r'invoice/add/$', views.orderInitDetails, name='orderDetails'),
    url(r'invoice/add/selectProducts/(?P<id>\d+)/', views.select_products_for_order, name='product-order'),
    url(r'invoice/add/selectCustomer/(?P<id>\d+)/', views.accept_customer_record, name='customer-records'),
    url(r'invoice/add/customer/(?P<id>\d+)/address/(?P<cust_id>\d+)/$', views.accept_customer_address, name='customer-address'),
    url(r'invoice/add/payment/(?P<id>\d+)/', views.payment, name='order-payment'),
    url(r'invoice/add/finalInvoice/(?P<id>\d+)/', views.generate_invoice, name='final-invoice'),

    # Delete Views
    url(r'invoice/(?P<po_id>\d+)/delete/', views.delete_product_order, name='product_order_delete'),
]
