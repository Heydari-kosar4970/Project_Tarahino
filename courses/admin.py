from django.contrib import admin
from .models import *


@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'teacher_name']


@admin.register(CourseHeadlinesModel)
class CourseHeadlinesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

