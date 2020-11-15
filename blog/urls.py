"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home_page, header, footer, resume_page, custom404, custom500
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_page),
    path('resume', resume_page),
    path('', include('blog_blog.urls')),
    path('', include('tinymce.urls')),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


handler404 = 'blog.views.custom404'
handler500 = 'blog.views.custom500'

if settings.DEBUG:
    # add root static files
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)