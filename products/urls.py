from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list_filter, name='products_list'),
    path('thanka-paintings-list/', views.thanka_paintings_view, name='thanka_paintings_list'),
    path('<int:product_id>/detail/', views.product_detail, name='product_detail'),
    path('mandala-list/', views.mandala_view, name='mandala_list'),
    path('gods-goddesses-list/', views.gods_goddesses_view, name='gods_goddesses_list'),
]
