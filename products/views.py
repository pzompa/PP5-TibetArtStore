from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import Product, Category
from checkout.models import Order
from .forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count



def products_list_filter(request):
    """ view to display all products"""
    # GET DATA from DB
    category = request.GET.get('category')
    sorting = request.GET.get('sorting')
    products = Product.objects.annotate(comment_count=Count('productcomment'))

    # Filter DATA
    if category and category != 'all':
        products = products.filter(productCategory_id=category)

    # Sort DATA
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
     # remove full/ string
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })
        paginator = Paginator(modified_products, 20) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'category': category,
        'sorting': sorting,
        'page_obj': page_obj
    }

    return render(request, 'products/products_list.html', context)


def product_detail(request, product_id):
    """ view to display details of a particular product"""
    product = get_object_or_404(Product, id=product_id)

    image_name = str(product.productImageName)

    if image_name.startswith('full/'):
        image_name = image_name[5:]

    context = {
        'product': product,
        'product_image_name': image_name,
        'product_id': product_id
    }

    return render(request, 'products/product_detail.html', context)



def thangka_paintings_view(request):
    """ view to display only Thangka paintings"""
    category = get_object_or_404(Category, name="thangka-paintings")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))
    

    # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {
        'products': page_obj,
    }

    return render(request, 'products/thangka_paintings_list.html', context)


def mandala_view(request):
    """ view to display all mandala Paintings"""
    category = Category.objects.get(name="mandalas")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))

        # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'products/mandala_list.html', context)

def gods_goddesses_view(request):
    category = Category.objects.get(name="gods-goddesses")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))

        # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'products/gods_goddesses_list.html', context)


def singing_bowls_view(request):
    """ view to display all singing bowls"""
    category = Category.objects.get(name="singing-bowls")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))

        # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'products/singing_bowls_list.html', context)


def crafts_view(request):
    """ view to display all the crafts products"""
    category = Category.objects.get(name="crafts")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))

        # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)

        if image_name.startswith('full/'):

            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'products/crafts_list.html', context)


def specials_view(request):
    """ view to display all special products"""
    category = Category.objects.get(name="specials")
    products = Product.objects.filter(productCategory=category).annotate(comment_count=Count('productcomment'))

        # Sort DATA
    sorting = request.GET.get('sorting')
    sort_map = {
        'name_asc': 'title',
        'name_desc': '-title',
        'price_asc': 'price',
        'price_desc': '-price',
    }
    sort_key = sort_map.get(sorting, 'title') 
    products = products.order_by(sort_key)

    modified_products = []
    
    for product in products:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]

        modified_products.append({
            'product': product,
            'image_name': image_name,
            'comment_count': product.comment_count
        })

    paginator = Paginator(modified_products, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }

    return render(request, 'products/specials_list.html', context)


def search_view(request):
    query = request.GET.get('q')
    if query:
        query_set = (
            Q(title__icontains=query) |
            Q(price__icontains=query) |
            Q(sku__icontains=query) |
            Q(description__icontains=query) |
            Q(liquid__icontains=query) |
            Q(productImageLink__icontains=query) |
            Q(productImageLinks__icontains=query) |
            Q(productKey__icontains=query) |
            Q(productCategory__name__icontains=query)
        )
        results = Product.objects.filter(query_set)
    else:
        results = Product.objects.all()
    
    modified_products = []
    for product in results:
        image_name = str(product.productImageName)
        if image_name.startswith('full/'):
            image_name = image_name[5:]
        
        modified_products.append({
            'product': product,
            'image_name': image_name
        })

    context = {
        'results': modified_products,
    }

    return render(request, 'products/search_results.html', context)

@login_required
def create_product(request):
    """ view to add a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!',)
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/create_product.html', context)

@login_required
def update_product(request, product_id):
    """ view to update a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')


    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully!')
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(request, 'Failed to update the product. Please try again.')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/update_product.html', context)

@login_required
def delete_product(request, product_id):
    """ View to delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted!')
    return redirect('products_list')

@login_required
def product_management(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    return render(request, 'products/product_management.html')

@login_required
def order_list(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'products/order_list.html', context)

@login_required
def delete_order(request, order_id):
    """ delete order """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, 'Order successfully deleted!')
    return redirect('product_management')