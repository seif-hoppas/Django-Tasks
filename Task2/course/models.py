from django.db import models
from instructor.models import Instructor
from student.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name