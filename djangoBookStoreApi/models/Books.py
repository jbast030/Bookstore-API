from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name