from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list_filter, name='products_list'),
    path('thanka-paintings-list/', views.thanka_paintings_view, name='thanka_paintings_list'),
]
