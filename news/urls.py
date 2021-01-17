from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('my-articles', views.my_articles, name="my_articles"),
    path('create-article', views.create_article, name="create_article")
]
