from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer  # Corrected spelling
from rest_framework.renderers import JSONRenderer

def student_data(request):
    student = Student.objects.get(id=1)  # Ensure student with id=1 exists
    serializer = StudentSerializer(student)
    
    json_renderer = JSONRenderer()
    json_data = json_renderer.render(serializer.data)  # Use the instance to call render

    return HttpResponse(json_data, content_type="application/json")  # Return the json_data
