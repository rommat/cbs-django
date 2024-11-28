from django.shortcuts import render
from django.http import HttpRequest
from .models import Student, Grade


# Create your views here.
def index(request: HttpRequest):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'main/index.html', context)


def student_grades(request: HttpRequest, student_id: int):
    student = Student.objects.get(id=student_id)
    grades = student.grades.all()
    context = {
        'student': student,
        'grades': grades,
        'page_title': f'{student.first_name} {student.last_name}'
    }

    return render(request, 'main/grades.html', context)
