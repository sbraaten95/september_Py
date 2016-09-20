from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='course_index'),
    url(r'^add$', views.add, name='course_add'),
    url(r'^destroy/(?P<id>\d+)$', views.commence, name='course_startdestroy'),
    url(r'^destroy/complete/(?P<id>\d+)$', views.complete, name='course_completedestroy')
]