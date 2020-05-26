from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics

from .models import Teacher, CityDict, CourseOrg
from .serializers import TeacherSerializer, CityDictSerializer, CourseOrgSerializer

# Create your views here.


class CityDictViewSet(viewsets.ModelViewSet):

    queryset = CityDict.objects.all()
    serializer_class = CityDictSerializer


class CourserOrgViewSet(viewsets.ModelViewSet):

    queryset = CourseOrg.objects.all()
    serializer_class = CourseOrgSerializer


class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


