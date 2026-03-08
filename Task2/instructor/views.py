from django.shortcuts import render, get_object_or_404
from .models import Instructor
from course.models import Course


def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructor_list.html", {"instructors": instructors, "active_nav": "instructors"})


def instructor_detail(request, id):
    instructor = get_object_or_404(Instructor, id=id)
    courses = instructor.course_set.prefetch_related('students').all()
    return render(request, "instructor_detail.html", {
        "instructor": instructor,
        "courses": courses,
        "active_nav": "instructors",
    })