from django.shortcuts import render, redirect
from .models import TestModel, UserTests
from courses.models import CourseModel
from collections import defaultdict


def load_dashboard_page(request):
    user_tests = UserTests.objects.filter(user_id=request.user).values_list('course_id', 'grade')
    result = defaultdict(list)

    for course_id, grade in user_tests:
        result[course_id].append(grade)
    return render(request, 'test/panel.html', {'user_tests': dict(result)})


def test_page(request, course_id):
    course_model = CourseModel.objects.get(id=course_id)
    questions = TestModel.objects.filter(course_id=course_id).order_by('?')[:6]
    wright = 0

    if request.method == 'POST':
        for question_id in request.POST.keys():
            if question_id != 'csrfmiddlewaretoken':
                user_question = TestModel.objects.get(course_id=course_id, id=question_id)
                if user_question is not None:
                    if __option_convertor(user_question.right_answer) == request.POST[question_id]:
                        wright += 1

        UserTests(user_id=request.user, course_id=course_model, grade=f'{wright}/6').save()
        return render(request, 'test/result.html', {'wright': wright})

    return render(request, 'test/test.html', {'questions': questions})


def __option_convertor(number):
    if number == 0:
        return 'first_option'
    if number == 1:
        return 'second_option'
    if number == 2:
        return 'third_option'
    if number == 3:
        return 'fourth_option'


