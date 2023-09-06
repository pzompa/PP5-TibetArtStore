
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_cart(request):
    """ A view to return the bag page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """
    
    cart = request.session.get('cart', {})
    product = Product.objects.get(pk=product_id)
    
    try:
        quantity = int(request.POST.get('quantity'))
        cart[product_id] = cart.get(product_id, 0) + quantity
    except TypeError:
        quantity = 1
        cart[product_id] = cart.get(product_id, 0) + quantity
        messages.success(request, f'Added {product.title} to your bag')
    redirect_url = request.POST.get('redirect_url', '/')
    
    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)



def update_cart(request, product_id):
    """ Update quantities in the cart """

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        
        if quantity > 0:
            cart[product_id] = quantity
        else:
            cart.pop(product_id, None)
        
        request.session['cart'] = cart

    return redirect(reverse('view_cart'))



def delete_from_cart(request, product_id):
    """Delete item from cart"""

    try:
        cart = request.session.get('cart', {})
        cart.pop(product_id, None)
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
