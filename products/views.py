from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Q


def products_list_filter(request):
    # GET DATA from DB
    category = request.GET.get('category')
    price_range = request.GET.get('price_range')
    sorting = request.GET.get('sorting')

    products = Product.objects.all()

    # Filter DATA
    if category and category != 'all':
        products = products.filter(productCategory_id=category)
    if price_range == '<100':
        products = products.filter(price__lt=100)
    elif price_range == '<1000':
        products = products.filter(price__lt=1000)
    elif price_range == '<5000':
        products = products.filter(price__lt=5000)

    # Sort DATA
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    # remove full/ string
    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            print(f"Stripping 'full/' from {image_name}")
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'products': modified_products,
        'category': category,
        'price_range': price_range,
        'sorting': sorting
    }

    return render(request, 'products/products_list.html', context)


def thanka_paintings_view(request):
    category = Category.objects.get(name="thangka-paintings")
    products = Product.objects.filter(productCategory=category)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'products': modified_products,
    }

    return render(request, 'products/thanka_paintings_list.html', context)


def product_detail(request, product_id):
    """ view to display all products"""

    product = get_object_or_404(Product, id=product_id)

    image_name = str(product.productImageName)

    if image_name.startswith('full/'):
        image_name = image_name[5:]

    context = {
        'product': product,
        'product_image_name': image_name
    }

    return render(request, 'products/product_detail.html', context)


def mandala_view(request):
    category = Category.objects.get(name="mandalas")

    products = Product.objects.filter(productCategory=category)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'products': modified_products,
    }

    return render(request, 'products/mandala_list.html', context)


def gods_goddesses_view(request):
    category = Category.objects.get(name="gods-goddesses")

    products = Product.objects.filter(productCategory=category)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'products': modified_products,
    }

    return render(request, 'products/gods_goddesses_list.html', context)

def singing_bowls_view(request):
    category = Category.objects.get(name="singing-bowls")

    products = Product.objects.filter(productCategory=category)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'products': modified_products,
    }

    return render(request, 'products/singing_bowls_list.html', context)