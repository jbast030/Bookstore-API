from django.db import models
from .books import Book

class BookDetails(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return f"BookDetails {self.id}"
