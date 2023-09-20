
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('favorite_products/', views.favorite_products, name='favorite_products'),
]
