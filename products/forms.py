from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productCategory', 'title', 'price', 'sku', 'description', 'liquid', 'productImageName','productImageNameFull','productImageNameSmall') 
