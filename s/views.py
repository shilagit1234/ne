from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
class StudentApi(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer