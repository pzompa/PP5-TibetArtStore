from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.blogpost_list, name='blogpost_list'),
    path('<int:pk>/', views.blogpost_detail, name='blogpost_detail'),
    # blogpost management
    path('create/', views.create_blogpost, name='create_blogpost'),
    path('save/', views.save_blogpost, name='save_new_blogpost'),
    path(
        'save/<int:blogpost_id>/',
        views.save_blogpost,
        name='save_update_blogpost'
    ),
    path('edit-list/', views.edit_list_blogpost, name='edit_list_blogpost'),
    path('edit/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
    path(
        'delete-list/',
        views.delete_list_blogpost,
        name='delete_list_blogpost'
    ),
    path(
        'delete/<int:blogpost_id>/',
        views.delete_blogpost,
        name='delete_blogpost'),
]
