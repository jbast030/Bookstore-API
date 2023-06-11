from django.db import models
from .users import User
from .books import Book

class BookComments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"BookComment {self.id}"
