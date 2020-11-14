from django.shortcuts import render
from blog_info.models import PersonalInfo

def contact_info(request):

    personal_info = PersonalInfo.objects.first()
    print(personal_info)
    context ={
        'personal_info': personal_info
    }
    return render(request, 'contact_page.html', context)