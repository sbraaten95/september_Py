from django.conf.urls import url
from . import views, destroy
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^addUser', views.addUser),
    url(r'^(?P<id>\d+)/destroy$', destroy)
]