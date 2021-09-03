import sqlite3
from django.shortcuts import render
from .connection import Connection
from bangazonapi.models import Order


def completed_order_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute("""
                SELECT ord.id as OrderId, pay.merchant_name as PaymentType, SUM(prod.price) as OrderTotal, user.first_name || " " || user.last_name as FullName
                FROM bangazonapi_order as ord, bangazonapi_payment as pay, 
                        bangazonapi_orderproduct as ordprod, bangazonapi_product as prod,
                        auth_user as user
                WHERE ord.payment_type_id = pay.id AND ord.id = ordprod.order_id
                    AND ordprod.product_id = prod.id AND ord.customer_id = user.id
                GROUP BY (ord.id);
            """)
            dataset = db_cursor.fetchall()

            order_list = []

            for row in dataset:
                order = Order()
                order.customer_name = row["FullName"]
                order.payment_type_name = row["PaymentType"]
                order.total = row["OrderTotal"]
                order.order_id = row["OrderId"]
                order_list.append(order)
        template = 'completed_orders.html'
        context = {
            'completed_order_list': order_list
        }
        return render(request, template, context)