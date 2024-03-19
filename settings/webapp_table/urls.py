# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('students/', students, name='students'),
    path('faculty/', faculty, name = 'faculty'),
    path('library/', books, name = 'books' ),
    path('courses/', course_item, name = 'courses')
]
