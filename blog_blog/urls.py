from django.urls import path, re_path, include
from .views import  blog_home_page,post_detail, posts_categories_partial, posts_by_category, search_posts_view



urlpatterns = [

   path('blog', blog_home_page),
   path('tag/<tag_slug>/', blog_home_page),
   # path('blog/notfound', search_result_none),
   path('blog/<postId>/<title>', post_detail),
   path('blog/<category_name>', posts_by_category, name="category_name"),
   path('blog/search/', search_posts_view),
   # path('blog-categories', posts_categories_partial,name='blog_categories'),


]