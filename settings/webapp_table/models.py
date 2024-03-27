# models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=12, primary_key=True)
    dob = models.DateField()
    ph_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=50)
    stud_class = models.CharField(max_length=50)
    stud_year = models.IntegerField()

    class Meta:
        db_table = 'students'  # Set the table name to 'students'
        

class faculties(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True, unique=True)
    teacher_name = models.CharField(max_length=100)
    teacher_qualification = models.CharField(max_length=100)
    teacher_degrees = models.TextField()  # Changed to TextField
    teacher_speciality = models.CharField(max_length=100)
    teacher_certificate = models.CharField(max_length=100)
    teacher_class_issued = models.CharField(max_length=100)
    teacher_subjects = models.TextField()  # Changed to TextField
    teacher_contact = models.CharField(max_length=20)
    teacher_email = models.EmailField(max_length=100)
    teacher_post = models.CharField(max_length=100)

    class Meta:
        db_table = 'faculty'
        
        

class library(models.Model):
    book_id = models.CharField(max_length=20, primary_key=True)
    book_name = models.CharField(max_length=100, unique=True)
    book_subject = models.CharField(max_length=100)
    book_class = models.CharField(max_length=50)
    book_author = models.CharField(max_length=100)
    book_status = models.CharField(max_length=50)
    book_publisher = models.CharField(max_length=100)
    book_issued_to = models.CharField(max_length=100, blank=True, null=True)
    book_count = models.IntegerField(default=0)
    book_year = models.IntegerField()
    
    class Meta:
        db_table = 'library'
        

class course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_books = models.TextField()
    course_subject = models.CharField(max_length=100)
    course_year = models.CharField(max_length=5)
    
    class Meta:
        db_table = 'courses'