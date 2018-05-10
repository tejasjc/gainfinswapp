"""Gainfins URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Cv import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tejasjc/$', views.cv_tejas,name='cv_tejas'),
    url(r'^rushikeshsp/$', views.cv_rushikesh,name='cv_rushikesh'),
    url(r'^sopan/$', views.cv_sopan,name='cv_sopan'),
    url(r'^shubham/$', views.cv_shubham,name='cv_shubham'),
    url(r'^cv/', include('Cv.urls')),
    url(r'^',include('Home.urls')),
]
