from django.db import models
from blogpost.models import BlogPost

class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_text = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.CharField(max_length=255, null=True, blank=True)