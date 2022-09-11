from django.shortcuts import render
from .models import *


def courses_page(request):
    return render(request, 'courses/course_list.html')


def single_course_page(request, course_id):
    selected_course = CourseModel.objects.filter(id=course_id).first()
    headlines = CourseHeadlinesModel.objects.filter(course_id=course_id)
    return render(request, 'courses/single_course.html', {'course': selected_course, 'headlines': headlines})
