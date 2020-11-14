from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models
from blog_blog.models import Comment
from ckeditor.widgets import CKEditorWidget


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'publish', 'status')
    list_filter = ('created', 'publish', 'status', 'author')
    search_fields = ('title', 'body')
    ordering = ('status', 'publish')

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
        }

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
