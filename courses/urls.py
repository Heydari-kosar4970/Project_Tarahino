from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.courses_page, name='courses_page'),
    path('single_course/<course_id>', views.single_course_page, name='single_course_page'),
]
