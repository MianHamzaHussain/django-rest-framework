from django.urls import path
from .views import student_data
urlpatterns = [
    path("",student_data,name="index")
]
