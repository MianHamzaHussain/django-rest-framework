from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
     class meta:
        model=Student,
        fields=['name','roll','city']
