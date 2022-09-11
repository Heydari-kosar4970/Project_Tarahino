from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard', load_dashboard_page, name='load_dashboard_page'),
    path('test/<course_id>', test_page, name='test_page'),
]