from django.shortcuts import render, get_object_or_404
from .models import Student
from course.models import Course


def student_list(request):
    students = Student.objects.all()
    return render(request, "student/student_list.html", {"students": students, "active_nav": "students"})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.filter(students=student)
    return render(request, "student/student_detail.html", {
        "student": student,
        "courses": courses,
        "active_nav": "students",
    })
