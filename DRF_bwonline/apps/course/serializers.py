from rest_framework import serializers

from .models import BannerCourse, Course
from organization.serializers import TeacherSerializer


class CourseSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    teacher = TeacherSerializer()

    class Meta:

        model = Course
        fields = '__all__'


class BannerCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = BannerCourse
        fields = ('__all__')
