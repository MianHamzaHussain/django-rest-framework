# Django REST Framework Project

This project demonstrates how to set up a Django REST framework application. It includes creating models, serializers, views, and routes to handle RESTful requests.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Key Concepts](#key-concepts)
- [Code](#code)

## Prerequisites

- Python 3.x
- Django
- Django REST Framework

## Setup Instructions

1. **Create a Python virtual environment**:
   ```bash
   python -m venv env

2. Activate the virtual environment:
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows

3. Install Django and Django REST Framework:
pip install django
pip install djangorestframework

4. Create a new Django project:
django-admin startproject rest_project
cd rest_project

5. Create a new Django app:
python manage.py startapp rest_app

6. Navigate to the rest_project directory.

7. Update settings.py: Add rest_framework and rest_app to the INSTALLED_APPS list:
INSTALLED_APPS = [
    ...
    'rest_framework',  # Add Django REST Framework to installed apps
    'rest_app',        # Register the rest_app application
]

8. Create the model: In rest_app/models.py, define your model:
from django.db import models
from django.contrib import admin

# Define the Student model with fields for name, roll number, and city
class StudentModel(models.Model):
    name = models.CharField(max_length=50)  # Student's name
    roll = models.IntegerField()              # Student's roll number
    city = models.CharField(max_length=50)   # Student's city

9. Go to Admin.py in my_project
# Register your model in the admin interface
from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
 list_display=['id','name',"rollno"]
admin.site.register(Student)

10. Create serializers: Create a file named serializers.py in the rest_app directory:
from rest_framework import serializers
from .models import StudentModel  # Import the model

# Define a serializer for the Student model
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city =serializers.CharField(max_length=50)


11. Create views: In rest_app/views.py, define your view function:
from django.shortcuts import render, HttpResponse
from .models import StudentModel  # Corrected import for the model
from .serializers import StudentSerializer  # Import the serializer
from rest_framework.renderers import JSONRenderer

# View function to return student data as JSON
def student_data(request):
    student = StudentModel.objects.get(id=1)  # Fetch student with id=1
    serializer = StudentSerializer(student)  # Serialize the student instance
    
    # Render the serialized data as JSON
    json_renderer = JSONRenderer()
    json_data = json_renderer.render(serializer.data)  # Convert to JSON

    return HttpResponse(json_data, content_type="application/json")  # Return JSON response

12. Create URLs for the app: Create a urls.py file in the rest_app directory:
from django.urls import path
from .views import student_data

urlpatterns = [
    path("", student_data, name="index")  # Route for the student_data view
]

13. Include app URLs in the project: In rest_project/urls.py, include the app's URLs:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', include("rest_app.urls")),  # Include the URLs from rest_app
]

14. Run database migrations:
python manage.py makemigrations  # Create migration files for changes in models
python manage.py migrate           # Apply migrations to the database

15. Create a superuser:
python manage.py createsuperuser  # Create a superuser for accessing the admin interface

16. Run the development server:
python manage.py runserver  # Start the development server


17. Handling Dynamic IDs and Fetching All Records
# To handle dynamic IDs and fetch all records, update rest_app/views.py as follows:
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import StudentModel
from .serializers import StudentSerializer

def student_data(request, pk):
    student = get_object_or_404(StudentModel, pk=pk)
    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data)

def students_data(request):
    students = StudentModel.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

# In rest_app/urls.py, update the URL patterns to handle the dynamic ID and list all student records:
from django.urls import path
from .views import student_data, students_data

urlpatterns = [
    path("student/<int:pk>/", student_data, name="student_detail"),
    path("students/", students_data, name="student_list"),
]


