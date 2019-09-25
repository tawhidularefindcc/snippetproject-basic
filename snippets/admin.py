from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path

from .models import Snippet

# Register your models here.
admin.site.site_header = 'Admin Panel Dashboard'

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created', )

admin.site.register(Snippet, SnippetAdmin)
admin.site.unregister(Group)