from django.shortcuts import render
# from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .serializers import CourseSerializer, BannerCourseSerializer, LessonSerializer, VideoSerializer, CourseResourceSerializer
from rest_framework import mixins
from rest_framework import viewsets
from .models import Course, BannerCourse, Lesson, Video, CourseResource
# Create your views here.


# 课程列表
class CourseViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# 轮播
class BannerCourseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = BannerCourse.objects.all()
    serializer_class = BannerCourseSerializer


# 课程章节
class LessonViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# 章节视频
class VideoViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Video.objects.all()
    serializer_class = VideoSerializer


# 课程资源
class CourseResourceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = CourseResource.objects.all()
    serializer_class = CourseResourceSerializer



