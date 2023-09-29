from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from products.models import Product
from blogpost.models import BlogPost
from .models import ProductComment, BlogPostComment
from .forms import ProductCommentForm, BlogPostCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count

def enter_comment(request, product_id):
    """
    Get Product and Comment, and generate the form.
    """
    product = Product.objects.get(pk=product_id)
    comments = ProductComment.objects.filter(product=product)
    form = ProductCommentForm()
    return render(request, 'comment/enter_comment.html', {
        'product': product,
        'comments': comments,
        'form': form,
        'edit_mode': False
    })

def new_blogpost_comment(request, blogpost_id):
    """
    Get Product and Comment, and generate the form.
    """
    blogpost = BlogPost.objects.get(pk=blogpost_id)
    comments = BlogPostComment.objects.filter(blogpost=blogpost)
    form = BlogPostCommentForm()
    return render(request, 'comment/new_blogpost_comment.html', {
        'blogpost': blogpost,
        'comments': comments,
        'form': form,
        'edit_mode': False
    })

@login_required
def save_comment(request, product_id, comment_id=None):
    """
    Save a new comment or update a specific comment of a authenticated user.
    """
    product = get_object_or_404(Product, pk=product_id)
    
    
    existing_comment = None
    if comment_id:
        existing_comment = ProductComment.objects.filter(pk=comment_id, product=product, user=request.user).first()

    if request.method == 'POST':
        form = ProductCommentForm(request.POST, instance=existing_comment)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.email = request.user.email
            comment.product = product
            comment.save()

            if existing_comment:
                messages.success(request, f'Comment updated successfully, {request.user.username}')
            else:
                messages.success(request, f'Comment added successfully, {request.user.username}')
            
            return redirect('enter_comment', product_id=product_id)
        else:
            comments = ProductComment.objects.filter(product=product)
            return render(request, 'comment/enter_comment.html', {
                'product': product,
                'comments': comments,
                'form': form
            })
    else:
       
       
        return redirect('enter_comment', product_id=product_id)

@login_required
def save_blogpost_comment(request, blogpost_id, comment_id=None):
    """
    Save a new comment or update a specific comment of a authenticated user.
    """
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    
   
    existing_comment = None
    if comment_id:
        existing_comment = BlogPostComment.objects.filter(pk=comment_id, blogpost=blogpost, user=request.user).first()

    if request.method == 'POST':
        form = BlogPostCommentForm(request.POST, instance=existing_comment)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.email = request.user.email
            comment.blogpost = blogpost
            comment.save()

            if existing_comment:
                messages.success(request, f'BlogPost comment updated successfully, {request.user.username}')
            else:
                messages.success(request, f'BlogPost Comment added successfully, {request.user.username}')
            
            return redirect('new_blogpost_comment', blogpost_id=blogpost_id)
        else:
            comments = BlogPostComment.objects.filter(blogpost=blogpost)
            return render(request, 'comment/new_blogpost_comment.html', {
                'blogpost': blogpost,
                'comments': comments,
                'form': form
            })
    else:
       
        return redirect('new_blogpost_comment', blogpost_id=blogpost_id)

@login_required
def delete_comment(request, comment_id):
    """
    Delete a specific comment if it belongs to the currently authenticated user.
    """
    comment = get_object_or_404(ProductComment, id=comment_id)
    product_id = comment.product.id


    if comment.user == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
    else:
        messages.error(request, "You do not have permission to delete this comment.")


    return redirect('enter_comment', product_id=product_id)

@login_required
def delete_blogpost_comment(request, comment_id):
    """
    Delete a specific comment if it belongs to the currently authenticated user.
    """
    comment = get_object_or_404(BlogPostComment, id=comment_id)
    blogpost_id = comment.blogpost.id

   
    if comment.user == request.user:
        comment.delete()
        messages.success(request, "BlogPost Comment deleted successfully!")
    else:
        messages.error(request, "You do not have permission to delete this comment.")

   
    return redirect('new_blogpost_comment', blogpost_id=blogpost_id)

@login_required
def edit_comment(request, product_id, comment_id=None):
    """
    Edit a specific comment if it belongs to the currently authenticated user.
    """
    comment = get_object_or_404(ProductComment, id=comment_id)

   
    if comment.user != request.user:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('enter_comment', product_id=comment.product.id)

   
    if request.method == 'POST':
        form = ProductCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect('enter_comment', product_id=comment.product.id)

    else:
        form = ProductCommentForm(instance=comment)

    product = comment.product 
    comments = ProductComment.objects.filter(product=product)

    return render(request, 'comment/enter_comment.html', {
        'product': product,
        'comments': comments,
        'form': form,
        'edit_mode': True,
        'comment_id': comment_id
    })

@login_required
def edit_blogpost_comment(request, blogpost_id, comment_id=None):
    """
    Edit a specific comment if it belongs to the currently authenticated user.
    """
    comment = get_object_or_404(BlogPostComment, id=comment_id)

    if comment.user != request.user:
        messages.error(request, "You do not have permission to edit this comment.")
        return redirect('new_blogpost_comment', blogpost_id=comment.blogpost.id) 

   
    if request.method == 'POST':
        form = BlogPostCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'BlogPost Comment updated successfully!')
            return redirect('new_blogpost_comment', blogpost_id=comment.blogpost.id)

    else:
        form = BlogPostCommentForm(instance=comment)

    blogpost = comment.blogpost 
    comments = BlogPostComment.objects.filter(blogpost=blogpost)

    return render(request, 'comment/new_blogpost_comment.html', {
        'blogpost': blogpost,
        'comments': comments,
        'form': form,
        'edit_mode': True,
        'comment_id': comment_id
    })