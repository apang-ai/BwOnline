"""DRF_bwonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import xadmin

from django.urls import path, include, re_path
from django.views.static import serve
from DRF_bwonline.settings import MEDIA_ROOT
from course.views import CourseViewSet, BannerCourseViewSet

router = DefaultRouter()
# 课程列表
router.register(r'course', CourseViewSet, basename='course')
# 首页轮播
router.register(r'banners', BannerCourseViewSet, basename='banners')


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # 文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # drf文档，title自定义
    path('docs', include_docs_urls(title='即在线教育')),
    # 课堂列表页
    re_path('^', include(router.urls)),
    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
]
