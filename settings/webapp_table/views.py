# views.py
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required      # it restrict some pages access ,to access these pages user have to login



def home(request):
    return render(request, 'home.html')

@login_required(login_url=('login'))   
def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

@login_required(login_url=('login'))   
def faculty(request):
    faculty = faculties.objects.all()  # Retrieve all faculty members
    return render(request, 'faculty.html', {'faculty': faculty})

def books(request):
    books = library.objects.all()
    return render(request, 'library.html',{'books':books})

def course_item(request):
    courses = course.objects.all()
    return render(request,'courses.html',{'courses':courses})


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
            else:
                # Authentication failed
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutuser(request):
    
    logout(request)
    return redirect('home')


def  register(request):
    page='register'
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create a new user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
            
            user.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()
    context = {'form': form, 'page':page}
    return render(request, 'register.html', context)