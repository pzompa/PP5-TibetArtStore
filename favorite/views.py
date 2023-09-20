from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from django.contrib import messages
from favorite.models import Favorite
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f'Added to Favorite')
    return redirect(request.META.get('HTTP_REFERER', 'default_url'))

@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'Removed from Favorite')
    return redirect(request.META.get('HTTP_REFERER', 'default_url'))
    
@login_required
def favorite_products(request):
    user = request.user
    favorite_products = Favorite.objects.filter(user=user)
    return render(request, 'favorite/favorite_products.html', {'favorite_products': favorite_products})
