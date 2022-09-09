from django.urls import path
from articles.views import *

urlpatterns = [
    path('articles', articles_page, name='articles_page'),
    path('uiux', uiux_page, name='uiux_page'),

]

