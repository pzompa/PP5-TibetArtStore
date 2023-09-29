from django.urls import path
from . import views

urlpatterns = [
    # PRODUCT
    path('enter/<int:product_id>/', views.enter_comment, name='enter_comment'),
    path('save/<int:product_id>/', views.save_comment, name='save_comment_new'),
    path('save/<int:product_id>/<int:comment_id>/', views.save_comment, name='save_comment_edit'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('edit/<int:product_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),

]
