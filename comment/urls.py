from django.urls import path
from . import views


urlpatterns = [
    # PRODUCT
    path(
        'enter/<int:product_id>/',
        views.enter_comment, name='enter_comment'
    ),
    path(
        'save/<int:product_id>/',
        views.save_comment,
        name='save_comment_new'
    ),
    path(
        'save/<int:product_id>/<int:comment_id>/',
        views.save_comment,
        name='save_comment_edit'
    ),
    path(
        'delete/<int:comment_id>/',
        views.delete_comment, name='delete_comment'
    ),
    path(
        'edit/<int:product_id>/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
    ),

    # BLOGPOST
    path(
        'new-blogpost-comment/<int:blogpost_id>/',
        views.new_blogpost_comment,
        name='new_blogpost_comment'
    ),
    path(
        'save-blogpost/<int:blogpost_id>/',
        views.save_blogpost_comment,
        name='save_blogpost_comment_new'
    ),
    path(
        'save-blogpost/<int:blogpost_id>/<int:comment_id>/',
        views.save_blogpost_comment,
        name='save_blogpost_comment_edit'
    ),
    path(
        'delete-blogpost/<int:comment_id>/',
        views.delete_blogpost_comment,
        name='delete_blogpost_comment'
    ),
    path(
        'edit-blogpost/<int:blogpost_id>/<int:comment_id>/',
        views.edit_blogpost_comment,
        name='edit_blogpost_comment'
    ),
]
