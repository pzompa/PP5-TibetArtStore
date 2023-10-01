
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_cart(request):
    """ A view to return the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping cart """
    
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)

    product_id_str = str(product_id)

    try:
        quantity = int(request.POST.get('quantity'))
    except TypeError:
        quantity = 1
        print(TypeError)

    if product_id_str in cart:
        cart[product_id_str] += quantity
        messages.success(request, f'Updated {product.title} quantity to {cart[product_id_str]}')
    else:
        cart[product_id_str] = quantity
        messages.success(request, f'Added {product.title} to your cart.')

    redirect_url = request.POST.get('redirect_url', '/')
    
    request.session['cart'] = cart

    return redirect('products')

def update_cart(request, product_id):
    """ Update quantities in the cart """
    
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        
        if quantity > 0:
            if product_id in cart and cart[product_id] != quantity:
                messages.success(request, f'Product quantity updated successfully!')
            cart[product_id] = quantity
        else:
            if product_id in cart:
                cart.pop(product_id, None)
                messages.warning(request, f'Product removed from the cart.')
            else:
                messages.warning(request, 'No item in the cart to remove.')
        

        request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def delete_from_cart(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
        cart = request.session.get('cart', {})
        
        if str(product_id) in cart:
            cart.pop(str(product_id))
            request.session['cart'] = cart
            messages.success(request, f'Removed {product.title} from your cart.')
            return HttpResponse(status=200)
        else:
            messages.warning(request, f'{product.title} was not found in your cart.')
            return HttpResponse(status=404)
        
    except Exception as e:
        messages.error(request, f'Error deleting the product.')
        return HttpResponse(status=500)
