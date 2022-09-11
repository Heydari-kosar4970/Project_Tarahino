from django.db.models import *
from courses.models import CourseModel
from django.conf import settings


TEST_CHOICE = [
    (0, 'گزینه اول'),
    (1, 'گزینه دوم'),
    (2, 'گزینه سوم'),
    (3, 'گزینه چهارم'),
]


class TestModel(Model):
    course_id = ForeignKey(CourseModel, on_delete=CASCADE)
    question = CharField(max_length=300, null=True)
    right_answer = IntegerField(choices=TEST_CHOICE)
    first_option = CharField(max_length=200, null=True)
    second_option = CharField(max_length=200, null=True)
    third_option = CharField(max_length=200, null=True)
    fourth_option = CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.course_id} - {self.question}'


class UserTests(Model):
    user_id = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    course_id = ForeignKey(CourseModel, on_delete=CASCADE, null=True)
    grade = CharField(max_length=4, null=True)
    create_at = DateTimeField(auto_now=True, null=True)
