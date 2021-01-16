from django.shortcuts import render

from .models import News

def home(request):

    context = {
        'news': News.objects.all()
    }

    return render(request, 'news/home.html', context=context)
