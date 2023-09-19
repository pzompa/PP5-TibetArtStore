from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    productImageName = models.ImageField(upload_to='full/')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    sku = models.CharField(max_length=200)
    description = models.TextField()
    liquid = models.TextField(blank=True)
    productImageLink = models.TextField(blank=True, null=True)  # Primary image link
    productImageLinks = models.TextField(blank=True, null=True)  # Serialized list for additional images
    productKey = models.CharField(max_length=250, blank=True, null=True)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    favorited_by = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def __str__(self):
        return self.title