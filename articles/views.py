from django.shortcuts import render
from .models import *


def articles_page(request):
    articles = ArticleModel.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})


def single_article_page(request, article_id):
    article = ArticleModel.objects.get(id=article_id)
    return render(request, 'articles/single_article.html', {'article': article})


