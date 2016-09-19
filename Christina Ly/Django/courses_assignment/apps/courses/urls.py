from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^destroy/(?P<id>\d+)$', views.destroyconfirm),
    url(r'^deleted$', views.destroy)
]
