from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from products.models import Product
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def add_to_favorites(request, id):
    product = get_object_or_404(Product, id=id)
    if product.favorited_by.filter(id=request.user.id).exists():
        product.favorited_by.remove(request.user)
        messages.success(request, 'Removed from favorites!')
    else:
        product.favorited_by.add(request.user)
        messages.success(request, 'Added to favorites!')

    return HttpResponseRedirect(request.META["HTTP_REFERER"],)


@login_required
def favorite_products(request):
    favorite_products = request.user.favorited_by.all()
    return render(request, 'favorite/favorite_products.html', {'favorite_products': favorite_products})
