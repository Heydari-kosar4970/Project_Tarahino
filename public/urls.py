from django.urls import path
from public.views import *

urlpatterns = [
    path('', index_page, name='index_page'),
    path('contactus', contactus_page, name='contactus_page'),
    path('aboutus', aboutus_page, name='aboutus_page'),

]





