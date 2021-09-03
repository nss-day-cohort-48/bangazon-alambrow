from django.conf.urls import url
from bangazonreports.views import expensive_products_list, completed_order_list, incomplete_order_list

urlpatterns = [
    url('reports/expensive_products', expensive_products_list),
    url('reports/completed_orders', completed_order_list),
    url('reports/incomplete_orders', incomplete_order_list),
]
