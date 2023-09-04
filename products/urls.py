from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list_filter, name='products_list'),
]
