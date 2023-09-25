from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from django.contrib import messages
from favorite.models import Favorite
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
# from products.urls import product_detail

# Product Detail page
@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f'Added to Favorite')
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'Removed from Favorite')
    return redirect(reverse('product_detail', args=[product_id]))


# Product List page
@login_required
def add_to_favorites_product_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f'Added to Favorite')
    return redirect('products')


@login_required
def remove_from_favorites_product_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'Removed from Favorite')
    return redirect('products')

# Favorite List page
@login_required
def remove_from_favorites_list(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'Removed from Favorite')
    return redirect('favorite_products') 

# Generate Favorite page
@login_required
def favorite_products(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    favorite_products = [favorite.product for favorite in favorites]
    return render(request, 'favorite/favorite_products.html', {'favorite_products': favorite_products, 'on_favorite_page': True})
