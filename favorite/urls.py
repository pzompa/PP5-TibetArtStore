
from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns = [
    path('add_to_favorites/<int:id>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorite_products/', views.favorite_products, name='favorite_products'),
]
