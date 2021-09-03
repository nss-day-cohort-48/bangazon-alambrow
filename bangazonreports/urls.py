from django.conf.urls import url
from bangazonreports.views import expensive_products_list, completed_order_list, inexpensive_products_list

urlpatterns = [
    url('reports/expensive_products', expensive_products_list),
    url('reports/inexpensive_products', inexpensive_products_list),
    url('reports/completed_orders', completed_order_list),
]
