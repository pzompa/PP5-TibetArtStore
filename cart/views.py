
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def view_cart(request):
    """ A view to return the bag page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    cart = request.session.get('cart', {})
    
    try:
        quantity = int(request.POST.get('quantity'))
        cart[product_id] = cart.get(product_id, 0) + quantity
    except TypeError:
        quantity = 1
        cart[product_id] = cart.get(product_id, 0) + quantity
    
    redirect_url = request.POST.get('redirect_url', '/')
    
    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)



def update_cart(request):
    """ Update quantities in the cart """

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        
        cart = request.session.get('cart', {})
        
        if product_id in cart:
            cart[product_id] = quantity
        
        request.session['cart'] = cart

    return redirect('view_cart')
