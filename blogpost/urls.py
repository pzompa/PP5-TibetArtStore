from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.blogpost_list, name='blogpost_list'),
    path('<int:pk>/', views.blogpost_detail, name='blogpost_detail'),
]