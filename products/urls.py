from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list_filter, name='products_list'),
    path('thangka-paintings-list/', views.thangka_paintings_view, name='thangka_paintings_list'),
    path('<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('mandala-list/', views.mandala_view, name='mandala_list'),
    path('gods-goddesses-list/', views.gods_goddesses_view, name='gods_goddesses_list'),
    path('singing-bowls-list/', views.singing_bowls_view, name='singing_bowls_list'),
    path('crafts-list/', views.crafts_view, name='crafts_list'),
    path('search_results/', views.crafts_view, name='search_results'),
    path('specials-list/', views.specials_view, name='specials_list'),
    path('add/', views.create_product, name='create_product'),
    path('<int:product_id>/edit/', views.update_product, name='update_product'),
    path('edit/<int:product_id>/', views.update_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('product-management/', views.product_management, name='product_management'),
    path('order-list/', views.order_list, name='order_list'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
]
