from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def article_list(request):
    active_articles = BlogPost.objects.filter(active=True)
    return render(request, 'blogpost/article_list.html', {'articles': active_articles})

def article_detail(request, pk):
    article = get_object_or_404(BlogPost, pk=pk)
    print(article.pk, pk)
    return render(request, 'blogpost/article_detail.html', {'article': article})
