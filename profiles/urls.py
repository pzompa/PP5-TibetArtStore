from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.display_profile, name='display_profile'),
    
]