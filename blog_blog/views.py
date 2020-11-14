from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView
from django.http import Http404
from .models import Post, Comment
from blog_category.models import PostCategory
from .forms import CommentForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from blog_info.models import PersonalInfo
from blog_blog.forms import PostForm


def blog_paginator(request, posts, page_number):

    categories = PostCategory.objects.all()
    paginator = Paginator(posts, page_number)  # posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)

    res = {
        'page': page,
        'post_list': post_list,
        'paginator': paginator,
        'categories': categories
    }
    return  res
    

def blog_home_page(request, tag_slug=None):

    published = Post.objects.get_published().order_by('-publish')
    categories = PostCategory.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        published = published.filter(tags__in = [tag])

    context = {
        'published':published,
    }
    context = {**context, **blog_paginator(request, published, 9)}
    return render(request, 'home_blog.html', context)



def posts_by_category(request, *args, **kwargs):
        
    category_name = kwargs['category_name']
    category = PostCategory.objects.filter(name__iexact= category_name).first()
    if category is None:
        raise Http404()
    posts= Post.objects.get_by_category(category_name)

    context={
        'published':posts,
    }
    context = {**context, **blog_paginator(request, posts,9)}

    return render(request, 'home_blog.html', context)


def posts_categories_partial(request):

    categories = PostCategory.objects.first()
    
    print(categories)

    context = {
        'categories': categories,
    }
    return render(request, 'posts_category_partial.html', context)



def post_detail(request, *args, **kwargs):

    selected_post_id = kwargs['postId']
    post = Post.objects.get_by_id(selected_post_id)
    if post is None :
        raise Http404()
        
    related_posts = Post.objects.get_queryset().filter(categories__post= post).distinct().exclude(id=selected_post_id)[:3]
    recent_posts = Post.objects.all().order_by('-publish').distinct().exclude(id=selected_post_id)[:3]
    featured_posts = Post.objects.get_published().annotate(total_comments=Count('comments')).order_by('-total_comments').distinct().exclude(id=selected_post_id)[:3]
    tags = Tag.objects.all()
    categories = PostCategory.objects.all()

    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        
        # comment has been added
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            name = comment_form.cleaned_data.get('name')
            email = comment_form.cleaned_data.get('email')
            body = comment_form.cleaned_data.get('body')
            Comment.objects.create(name=name, email=email, body=body, post=post )
            comment_form = CommentForm()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    personal_info = PersonalInfo.objects.first()
    form = PostForm()
    context = {
        'post': post,
        'related_posts': related_posts,
        'recent_posts': recent_posts,
        'featured_posts': featured_posts,
        'comments': comments,
        'comment_form': comment_form,
        'tags':tags,
        'categories':categories,
        'personal_info': personal_info, 
        'form':form
    }

    return render(request, 'post_detail.html', context)



def search_posts_view(request):

    query = request.GET.get('q')
    if query is not None:
        res = Post.objects.search(query)
        if not res:
            latest_posts = Post.objects.all().order_by('-publish').distinct()[:4]
            context = {
                'latest_posts': latest_posts
            }
            return render(request, 'search_none_result.html', context)

    else:
        res = Post.objects.get_published()
    
    context={
        'published':res,
    }
    context = {**context, **blog_paginator(request, res,9)}
    return render(request, 'home_blog.html', context)

