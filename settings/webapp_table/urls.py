# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('faculty/', faculty, name = 'faculty'),
    path('library/', books, name = 'books' ),
    path('courses/', course_item, name = 'courses'),
    
    path('registration/', register, name = 'register'),
    path('login/', custom_login, name='login'),
    path("logout/",logoutuser , name="logout"),
]
