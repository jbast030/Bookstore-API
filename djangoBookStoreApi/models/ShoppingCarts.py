from django.db import models
from .users import User

class ShoppingCarts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"ShoppingCart {self.id}"
