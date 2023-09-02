from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def products_list(request):
    """ view to display all products"""

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/products_list.html', context)


def product_detail(request, product_id):
    """ view to display all products"""

    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)

