from django.db.models import *


COURSE_TYPE = [
    ('آنلاین', 'ON'),
    ('آفلاین', 'OFF'),
]


class CourseModel(Model):
    title = CharField(max_length=100, null=True)
    sub_description = TextField(max_length=300, null=True)
    description = TextField(max_length=1000, null=True)
    cover = ImageField(upload_to='courseCover', null=True)
    duration = CharField(max_length=20)
    type = CharField(max_length=10, choices=COURSE_TYPE)
    teacher_name = CharField(max_length=50)
    teacher_introduction = TextField(max_length=200)

    def __str__(self):
        return self.title


class CourseHeadlinesModel(Model):
    course_id = ForeignKey(CourseModel, on_delete=CASCADE)
    title = CharField(max_length=100, null=True)
    video_link = URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.course_id} - {self.title}'

