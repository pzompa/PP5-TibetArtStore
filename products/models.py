from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    productImageName = models.ImageField(upload_to='full/', default='noimage.png',blank=True)
    productImageNameFull = models.ImageField(upload_to='full/', default='noimage.png',blank=True)
    productImageNameSmall = models.ImageField(upload_to='small/', default='noimage.png',blank=True)
    titleHTML = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    priceHTML = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    skuHTML = models.CharField(max_length=2000)
    sku = models.CharField(max_length=200)
    descriptionHTML = models.TextField()
    description = models.TextField()
    liquidHTML = models.TextField(blank=True)
    liquid = models.TextField(blank=True)
    productImageLink = models.TextField(blank=True, null=True)
    productImageLinks = models.TextField(blank=True, null=True)
    productKey = models.CharField(max_length=250, blank=True, null=True)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    favorited_by = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def __str__(self):
        return self.title