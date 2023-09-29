from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.db.models import Count

def blogpost_list(request):
    active_articles = BlogPost.objects.filter(active=True).annotate(comment_count=Count('blogpostcomment'))

    return render(request, 'blogpost/blogpost_list.html', {'articles': active_articles})

def blogpost_detail(request, pk):
    # article = get_object_or_404(BlogPost, pk=pk)
    article = BlogPost.objects.filter(pk=pk).annotate(comment_count=Count('blogpostcomment')).first()
    if not article:
        raise Http404("BlogPost not found")
    return render(request, 'blogpost/blogpost_detail.html', {'article': article})
