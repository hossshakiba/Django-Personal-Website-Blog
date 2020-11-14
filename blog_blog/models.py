from django.db.models import Q
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import operator
from functools import reduce
import os
from blog_category.models import PostCategory
from tinymce.widgets import TinyMCE
import math
from taggit.managers import TaggableManager
from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

def get_filename_extension(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_extension(filename)
    final_name = f'{instance.id}-{instance.title}{ext}'
    return f'blog/{final_name}'

     
class PostsManager(models.Manager):

    def get_published(self):
        return self.get_queryset().filter(status='published')

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact= category_name, status='published')

    
    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(tags__name__icontains=query)
        )
        return self.get_queryset().filter(lookup, status='published').distinct()



class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    body = RichTextUploadingField()   
    # body = tinymce_models.HTMLField()
    image = models.ImageField(upload_to=upload_image_path)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=10,choices= STATUS_CHOICES, default='draft')
    categories = models.ManyToManyField(PostCategory, blank=True)
    tags = TaggableManager(blank=True)


    objects = PostsManager()

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
       

    class Media:
        js = ('/site_media/static/tiny_mce/tinymce.min.js',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.id}/{self.title.replace(' ','-')}"

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.publish

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second"
            
            else:
                return str(seconds) + " seconds"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute"
            
            else:
                return str(minutes) + " minutes"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour"

            else:
                return str(hours) + " hours"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day"

            else:
                return str(days) + " days"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month"

            else:
                return str(months) + " months"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year"

            else:
                return str(years) + " years"

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default = True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



