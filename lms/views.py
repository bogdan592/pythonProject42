from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,)
# Create your views here.
from lms.models import Student, Curator
from lms.serializers import StudentSerializer, CuratorSerializer


class StudentViewSet(viewsets.Model.View.Set):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permissiom_classes = [IsAuthenticatedOrReadOnly]
class CuratorViewSet(viewsets.Model.View.Set):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permissiom_classes = [IsAuthenticatedOrReadOnly]