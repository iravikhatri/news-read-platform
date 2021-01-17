from django.shortcuts import render, redirect

from .models import News
from .forms import NewsForm

def home(request):

    context = {
        'news': News.objects.all()
    }

    return render(request, 'news/articles_list.html', context=context)


def my_articles(request):

    context = {
        'news': News.objects.filter(author=request.user)
    }

    return render(request, 'news/articles_list.html', context=context)


def create_article(request):
    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('my_articles')
    else:
        form = NewsForm()
    return render(request, 'news/article_create.html', {'form': form})
