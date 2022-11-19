from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,)
# Create your views here.
from lms.models import Student
from lms.serializers import StudentSerializer
class StudentViewSet(viewsets.Model.View.Set):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissiom_classes = [IsAuthenticatedOrReadOnly]