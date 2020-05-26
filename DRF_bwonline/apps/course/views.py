from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import CourseSerializer, BannerCourseSerializer, LessonSerializer, VideoSerializer, CourseResourceSerializer
from .models import Course, BannerCourse, Lesson, Video, CourseResource
from .filters import CourseFilter

# Create your views here.


# 自定义分页
class CoursePagination(PageNumberPagination):

    # 默认每页显示的个数
    page_size = 1
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


# 课程列表
class CourseViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset = Course.objects.all()
    # 分页
    pagination_class = CoursePagination
    # 序列化
    serializer_class = CourseSerializer
    # 过滤器
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置filter的类为我们自定义的类
    # 过滤
    filter_class = CourseFilter
    # 搜索,=name表示精确搜索，也可以使用各种正则表达式
    search_fields = ('=name', 'desc')
    # 排序
    ordering_fields = ('students', 'add_time')


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



