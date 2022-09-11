from .models import CourseModel


def courses_list(request):
    courses = CourseModel.objects.all()
    return {'courses': courses}
