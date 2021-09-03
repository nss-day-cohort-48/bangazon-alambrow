import sqlite3
from django.shortcuts import render
from .connection import Connection
from bangazonapi.models import Product

def inexpensive_products_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute("""
                SELECT prod.name, prod.price, prod.description 
                FROM bangazonapi_product as prod
                WHERE prod.price < 1000;
            """)
            dataset = db_cursor.fetchall()

            prod_list = []

            for row in dataset:
                product = Product()
                product.name = row["name"]
                product.price = row["price"]
                product.description = row["description"]
                prod_list.append(product)
        template = 'inexpensive_products_list.html'
        context = {
            'inexpensive_products_list': prod_list
        }
        return render(request, template, context)