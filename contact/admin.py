from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'date_created', 'comment')
    list_filter = ('date_created', 'name', 'email')
    search_fields = ('name', 'email', 'comment')
    ordering = ('-date_created',)


admin.site.register(Contact, ContactAdmin)