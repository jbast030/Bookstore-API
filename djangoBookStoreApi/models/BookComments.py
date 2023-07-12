from django.db import models
from .Users import Users
from .Books import Books

class BookComments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(null=True)

    # class Meta:
    #     ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user)
