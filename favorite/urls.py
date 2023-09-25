
from django.urls import path
from . import views


urlpatterns = [
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('add_to_favorites_product_list/<int:product_id>/', views.add_to_favorites_product_list, name='add_to_favorites_product_list'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('remove_from_favorites_product_list/<int:product_id>/', views.remove_from_favorites_product_list, name='remove_from_favorites_product_list'),
    path('remove_from_favorites_list/<int:product_id>/', views.remove_from_favorites_list, name='remove_from_favorites_list'),
    path('favorite_products/', views.favorite_products, name='favorite_products'),
]
