from django.shortcuts import render
# from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .serializers import CourseSerializer, BannerCourseSerializer
from rest_framework import mixins
from rest_framework import viewsets
from .models import Course, BannerCourse
# Create your views here.


class CourseViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BannerCourseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = BannerCourse.objects.all()
    serializer_class = BannerCourseSerializer



