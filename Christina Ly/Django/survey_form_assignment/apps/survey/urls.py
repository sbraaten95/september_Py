from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^survey/process$', views.process_users),
	url(r'^result$', views.result_users),
	url(r'^reset$', views.reset)
]