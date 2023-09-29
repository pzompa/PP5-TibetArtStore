from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import products_list_filter, search_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', products_list_filter, name='products_list'),
    path('products/', products_list_filter, name='products'),
    path('product/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('search/', search_view, name='search_view'),
    path('blogpost/', include('blogpost.urls')),
    path('aboutus/', include('aboutus.urls')),
    path('favorite/', include('favorite.urls')),
    path('contact/', include('contact.urls')),
    path('comment/', include('comment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
