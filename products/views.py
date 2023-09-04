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
