"""ApiProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings
from ApiApplication import views
from rest_framework import routers
from django.urls import include
router = routers.DefaultRouter()
router.register('api/v1/student', views.StudentsViewSet, basename='student')
router.register('api/v1/courses', views.CourseViewSet, basename='course')




urlpatterns = [
    # path('', include('ApiApplication.urls')),
    path('admin/', admin.site.urls),
    url("api/v1/person/",views.PersonApiView.as_view()),
    path('',include(router.urls)),
    # path('person/<int:id>/', include('ApiApplication.urls'))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
