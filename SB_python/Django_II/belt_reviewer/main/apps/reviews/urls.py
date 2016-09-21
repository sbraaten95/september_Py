from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home$', views.home, name='home'),
	url(r'^add$', views.add, name='one'),
	url(r'^submit$', views.submit, name='submit'),
	url(r'^newreview/(?P<id>\d+)$', views.newreview, name='newreview'),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
	url(r'^deletebook/(?P<id>\d+)$', views.deletebook, name='deletebook'),
	url(r'^showuser/(?P<id>\d+)$', views.showuser, name='showuser')
]