from django.shortcuts import render, redirect
from django.template import RequestContext
from blog_contact.forms import ContactForm
from blog_contact.models import Contact
from blog_blog.models import Post
from blog_info.models import PersonalInfo



def home_page(request):

    personal_info = PersonalInfo.objects.first()
    contact_form = ContactForm(request.POST or None)
    

    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('fullname')
        email = contact_form.cleaned_data.get('email')
        phone = contact_form.cleaned_data.get('phone')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
            
        Contact.objects.create(fullname=fullname, email=email, phone=phone, subject=subject, text=text, is_read=False)
        contact_form = ContactForm()
    
    blog_posts = Post.objects.get_published().order_by('-publish')[:5]
        

    context = {
        'blog_posts' : blog_posts,
        'contact_form': contact_form,
        'personal_info': personal_info,

    }
    return render(request, 'home_page.html', context)



def resume_page(request):
    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info':personal_info
    }
    return render(request, 'resume_page.html', context)


def custom404(request, exception=None):
    return render(request, '404.html', {})

def custom500(request, exception=None):
    return render(request, '500.html', {})


# header code behind 
def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Footer.html', context)



