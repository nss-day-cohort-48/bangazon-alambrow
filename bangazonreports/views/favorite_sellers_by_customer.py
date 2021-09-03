import sqlite3
from django.shortcuts import render
from .connection import Connection


def favorite_sellers_by_customer_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()
            db_cursor.execute("""
                SELECT user.first_name || " " || user.last_name as CustomerName, seller.first_name || " " || seller.last_name as SellerName
                FROM bangazonapi_favorite as fav, auth_user as user, auth_user as seller
                WHERE fav.customer_id = user.id AND fav.seller_id = seller.id;
            """)
            dataset = db_cursor.fetchall()

            favs = []

            # for row in dataset:
            #     customer = row["CustomerName"]
            #     seller = row["SellerName"]
            #     if customer in favs:
            #         favs[customer].append(seller)
            #     else:
            #         favs[customer].append(seller)

            for row in dataset:
                if row["CustomerName"] in favs:
                    favs[row["CustomerName"]].append(row["SellerName"])
                else:
                    favs[(row["CustomerName"])].append(row["SellerName"])


                
        template = 'favorite_sellers_by_customer.html'
        context = {
            'favorite_sellers_by_customer_list': favs
        }
        return render(request, template, context)