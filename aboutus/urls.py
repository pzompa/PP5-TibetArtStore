from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('aboutus/', views.service_policy, name='service_policy'),
    path('aboutus/', views.privacy_policy, name='privacy_policy')

]
