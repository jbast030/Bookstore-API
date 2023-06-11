from django.db import models
from .users import User

class WishLists(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"WishList {self.id}"
