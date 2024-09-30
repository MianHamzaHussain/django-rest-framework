from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer

def student_data(request, pk):
    # Fetch a student by primary key (id), or return a 404 error if not found
    student = get_object_or_404(Student, pk=pk)
    
    # Serialize the student instance
    serializer = StudentSerializer(student)
    
    # Return the serialized data as JSON
    return JsonResponse(serializer.data)

def students_data(request):
    # Fetch all students
    students = Student.objects.all()
    
    # Serialize the queryset (many=True)
    serializer = StudentSerializer(students, many=True)
    
    # Return the serialized data as JSON
    return JsonResponse(serializer.data, safe=False)
