from django.db import models
from .wish_lists import WishList
from .books import Book

class WishListBooks(models.Model):
    id = models.AutoField(primary_key=True)
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return f"WishListBook {self.id}"
