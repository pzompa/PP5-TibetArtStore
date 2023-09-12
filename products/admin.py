from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'sku', 'productCategory']
    search_fields = ['title', 'sku']
    list_filter = ['productCategory']

    ordering = ('sku',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
