from bangazonreports.views.inexpensive_products import inexpensive_products_list
from django.conf.urls import url
from bangazonreports.views import expensive_products_list, inexpensive_products_list, favorite_sellers_by_customer_list

urlpatterns = [
    url('reports/expensive_products', expensive_products_list),
    url('reports/inexpensive_products', inexpensive_products_list),
    url('reports/favorite_sellers_by_customer', favorite_sellers_by_customer_list)
]
