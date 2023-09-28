from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('service_policy/', views.service_policy, name='service_policy'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy')

]
