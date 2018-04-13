from django.conf.urls import url
from . import views
app_name='Cv'
urlpatterns = [
     url(r'^tejasjc/$', views.cv_tejas,name='cv_tejas'),
     url(r'^rushikeshsp/$', views.cv_rushikesh,name='cv_rushikesh'),
     url(r'^sopan/$', views.cv_sopan,name='cv_sopan'),
     url(r'^shubham/$', views.cv_shubham,name='cv_shubham'),
]
