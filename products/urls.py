from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('', views.products_list, name='products_list')
]
