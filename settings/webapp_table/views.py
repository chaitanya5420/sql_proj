# views.py
from django.shortcuts import render
from .models import *

def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def faculty(request):
    faculty = faculties.objects.all()  # Retrieve all faculty members
    return render(request, 'faculty.html', {'faculty': faculty})

def books(request):
    books = library.objects.all()
    return render(request, 'library.html',{'books':books})

def course_item(request):
    courses = course.objects.all()
    return render(request,'courses.html',{'courses':courses})