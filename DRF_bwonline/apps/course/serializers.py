from rest_framework import serializers

from .models import BannerCourse, Course, Lesson, Video, CourseResource
from organization.serializers import TeacherSerializer


# 课程
class CourseSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    teacher = TeacherSerializer()

    class Meta:

        model = Course
        fields = '__all__'


# 轮播
class BannerCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerCourse
        fields = '__all__'


# 课程章节
class LessonSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


# 章节视频
class VideoSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    lesson = LessonSerializer()

    class Meta:
        model = Video
        fields = '__all__'


# 课程资源
class CourseResourceSerializer(serializers.ModelSerializer):

    # 覆盖外键字段
    course = CourseSerializer()

    class Meta:

        model = CourseResource
        fields = '__all__'

