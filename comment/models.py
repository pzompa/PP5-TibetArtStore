from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Comment(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_text = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.CharField(max_length=255, null=True, blank=True)

class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username}: {self.comment_text[:50]}"
