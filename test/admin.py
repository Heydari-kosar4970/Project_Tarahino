from django.contrib import admin
from .models import *


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'question', 'right_answer']


@admin.register(UserTests)
class UserTestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'course_id', 'grade', 'create_at']

