from django.contrib import admin
from .models import PostCategory

# Register your models here.
class PostCategoryAdmin(admin.ModelAdmin):

    list_display= ['__str__','name']
    
    class Meta:
        model = PostCategory


admin.site.register(PostCategory, PostCategoryAdmin)