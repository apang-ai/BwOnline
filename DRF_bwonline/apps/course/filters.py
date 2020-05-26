import django_filters

from .models import Course


class CourseFilter(django_filters.rest_framework.FilterSet):
    '''
    商品过滤的类
    '''

    # 两个参数，name是要过滤的字段，lookup是执行的行为，
    students_min = django_filters.NumberFilter(field_name="students", lookup_expr='gte')
    students_max = django_filters.NumberFilter(field_name="students", lookup_expr='lte')

    class Meta:
        model = Course
        fields = ['students_min', 'students_max']