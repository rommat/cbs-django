from django.shortcuts import render
from django.http import HttpRequest
from .models import Student, Grade


# Create your views here.
def index(request: HttpRequest):
    students = Student.objects.all()
    context = {'students': students}

    return render(request, 'main/index.html', context)
