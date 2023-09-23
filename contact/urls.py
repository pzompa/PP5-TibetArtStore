from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email, name='send_email'),
    path('', views.send_email, name='contact_us')
]