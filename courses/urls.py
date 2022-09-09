from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.courses_page, name='courses_page'),
    path('courseadobexd', views.courseadobexd_page, name='courseadobexd_page'),
]
