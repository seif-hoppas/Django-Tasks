from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.select_related('instructor').all()
    return render(request, "course/course_list.html", {"courses": courses, "active_nav": "courses"})


def course_detail(request, id):
    course = get_object_or_404(Course.objects.select_related('instructor').prefetch_related('students'), id=id)
    return render(request, "course/course_detail.html", {"course": course, "active_nav": "courses"})
