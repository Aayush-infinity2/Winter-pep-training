from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializers import  StudentsSerializers

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = (Students.objects.all())
    serializer_class = StudentsSerializers

