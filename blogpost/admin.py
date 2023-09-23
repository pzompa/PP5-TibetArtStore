from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer_name', 'published_date', 'active')
    search_fields = ('title', 'writer_name')
    list_filter = ('published_date', 'active')

admin.site.register(BlogPost, BlogPostAdmin)