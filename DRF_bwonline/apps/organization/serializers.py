from rest_framework import serializers
from .models import Teacher, CityDict, CourseOrg


class CityDictSerializer(serializers.ModelSerializer):

    class Meta:

        model = CityDict
        fields = '__all__'


class CourseOrgSerializer(serializers.ModelSerializer):
    # 覆盖外键字段
    city = CityDictSerializer()

    class Meta:
        model = CourseOrg
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):

    # 覆盖外键字段
    org = CourseOrgSerializer()

    class Meta:

        model = Teacher
        fields = '__all__'
