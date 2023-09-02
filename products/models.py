from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    productImageName = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    description = models.TextField()
    liquid = models.TextField(blank=True)
    productImageLink = models.TextField()  # Primary image link
    productImageLinks = models.TextField()  # Serialized list for additional images
    productKey = models.CharField(max_length=250)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.title