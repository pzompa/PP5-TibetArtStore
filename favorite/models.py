from django.db import models
from django.contrib.auth.models import User
from products.models import Product 

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by_users')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product') 

    def __str__(self):
        return f"{self.user.username} favorited {self.product.title}"