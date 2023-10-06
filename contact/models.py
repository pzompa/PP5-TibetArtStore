from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    comment = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
