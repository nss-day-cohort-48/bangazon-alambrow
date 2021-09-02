from django.db import models
from django.db.models.deletion import CASCADE
from .customer import Customer
from .product import Product

class Like(models.Model):
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)