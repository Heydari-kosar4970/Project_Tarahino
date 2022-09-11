from django.urls import path
from articles.views import *

urlpatterns = [
    path('articles', articles_page, name='articles_page'),
    path('single_article/<article_id>', single_article_page, name='single_article_page'),

]

