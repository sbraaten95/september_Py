from django.conf.urls import url
# from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index), #index
    url(r'^emails$', views.create), #emails
    url(r'^success$', views.success),
    url(r'^emails/(?P<id>[0-9]*)/delete', views.destroy)
]
