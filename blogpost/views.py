from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.db.models import Count
from django.contrib import messages


def blogpost_list(request):
    active_articles = BlogPost.objects.filter(active=True).annotate(comment_count=Count('blogpostcomment'))

    return render(request, 'blogpost/blogpost_list.html', {'articles': active_articles})

def blogpost_detail(request, pk):
    # article = get_object_or_404(BlogPost, pk=pk)
    article = BlogPost.objects.filter(pk=pk).annotate(comment_count=Count('blogpostcomment')).first()
    if not article:
        raise Http404("BlogPost not found")
    return render(request, 'blogpost/blogpost_detail.html', {'article': article})


# Create BlogPost
def create_blogpost(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
    
            return redirect('list_blogposts')
    else:
        form = BlogPostForm()

    return render(request, 'blogpost/create_blogpost.html', {'form': form})

# Edit BlogPost
def edit_list_blogpost(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    blogposts = BlogPost.objects.all()
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blogpost/edit_list_blogpost.html', context)

def edit_blogpost(request, blogpost_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    if request.method == "post":
        form = BlogPostForm(request.POST, request.FILES, instance=blogpost)

        if form.is_valid():
            form.save()
            return redirect('blogpost/edit_list_blogpost')

    else:
        form = BlogPostForm(instance=blogpost)

    return render(request, 'blogpost/edit_blogpost.html', {'form': form})

# Delete BlogPost
def delete_list_blogpost(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    blogposts = BlogPost.objects.all()
    context = {
        'blogposts': blogposts,
    }
    return render(request, 'blogpost/delete_list_blogpost.html', context)

def delete_blogpost(request, blogpost_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store Admin can do this action.')
        return redirect('home')

    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    blogpost.delete()
    messages.success(request, 'Blog post deleted successfully!')

    return redirect('product_management')
    


# List BlogPost
# def list_blogposts(request):
#     pass

# List BlogPost
def save_blogpost(request, blogpost_id=None):
    if request.method == 'POST':
        instance = BlogPost.objects.get(pk=blogpost_id) if blogpost_id else None
        form = BlogPostForm(request.POST, request.FILES, instance=instance)
        
            
        if form.is_valid():
            is_new_blogpost = form.instance.pk is None
            
            form.save()
            
            if is_new_blogpost:
                messages.success(request, 'Blog post created successfully!')
            else:
                messages.success(request, 'Blog post updated successfully!')
            
            return redirect('product_management')
        else:
            messages.error(request, 'There was an error creating the blog post. Please check the form and try again.')
            return render(request, 'create_blogpost.html', {'form': form})
    else:
        return redirect('create_blogpost')