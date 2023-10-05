from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages
from favorite.models import Favorite
from django.contrib.auth.views import redirect_to_login

from django.urls import reverse


# Product Detail page
def add_to_favorites(request, product_id):
    if not request.user.is_authenticated:
        return redirect_to_login(next=reverse('product_detail', args=[product_id]))

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
def add_to_favorites_product_list(request, product_id):
    if not request.user.is_authenticated:
        return redirect_to_login(next=reverse('product_detail', args=[product_id]))

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
