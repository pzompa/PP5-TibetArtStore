from django.contrib import admin
from .models import ProductComment

class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'comment_text', 'user', 'date_time', 'email')  # Display these fields in the list view
    list_filter = ('product', 'user', 'date_time',)  # Add filters based on these fields
    search_fields = ('comment_text', 'user__username', 'email', 'product__title',)  # Search by these fields
    ordering = ('-date_time',)  # Latest comments first
    readonly_fields = ('date_time',)  # Makes the date_time field read-only in the admin site

admin.site.register(ProductComment, ProductCommentAdmin)
