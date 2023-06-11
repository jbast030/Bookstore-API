from django.db import models
from .shopping_carts import ShoppingCart
from .books import Book

class ShoppingCartBooks(models.Model):
    id = models.AutoField(primary_key=True)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return f"ShoppingCartBook {self.id}"
