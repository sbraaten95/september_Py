from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addNote$', views.addNote, name='addNote'),
    url(r'^getData$', views.getData, name='getData')
]
