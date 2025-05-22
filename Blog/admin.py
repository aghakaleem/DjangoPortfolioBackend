from django.contrib import admin
from django import forms
# Register your models here.

from django.contrib.auth import get_user_model
from .models import Post, PostSection, Comment, Like


User = get_user_model()


class PostSectionInline(admin.TabularInline):
    model = PostSection
    extra = 1
    fields = ['order', 'section_type', 'text', 'image']
    readonly_fields = ['order']
    ordering = ['order']
    show_change_link = True

class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']
    inlines = [PostSectionInline]
    list_filter = ['updated_at']
    ordering = ['-created_at', '-updated_at']
    

class PostSectionAdmin(admin.ModelAdmin):

    list_display = ['id', 'post', 'order', 'section_type', 'text', 'image']
    search_fields = ['post__title']
    list_filter = ['section_type']
    ordering = ['post', 'order']




admin.site.register(Post, PostAdmin)
admin.site.register(PostSection, PostSectionAdmin)
admin.site.register(Comment)
admin.site.register(Like)