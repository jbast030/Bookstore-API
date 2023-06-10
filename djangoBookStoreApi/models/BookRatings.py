from django.db import models
from .books import Book

class BookRatings(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.SmallIntegerField()

    def __str__(self):
        return f"BookRating {self.id}"
