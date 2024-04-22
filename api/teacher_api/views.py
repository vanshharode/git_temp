from django.shortcuts import render
from rest_framework import viewsets
from teacher_api.serializers import Teacherserializer
from teacher_api.models import Teacher

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = Teacherserializer

