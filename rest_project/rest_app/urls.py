from django.urls import path
from .views import student_data,students_data

urlpatterns = [
    path("student/<int:pk>/", student_data, name="student_detail"),  # Route for student by ID
    path("students/", students_data, name="student_list"),  # Route for listing all students
]
