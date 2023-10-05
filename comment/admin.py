from django.contrib import admin
from .models import ProductComment

class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'comment_text', 'user', 'date_time', 'email')
    list_filter = ('product', 'user', 'date_time',)
    search_fields = ('comment_text', 'user__username', 'email', 'product__title',)
    ordering = ('-date_time',) 
    readonly_fields = ('date_time',)

admin.site.register(ProductComment, ProductCommentAdmin)
