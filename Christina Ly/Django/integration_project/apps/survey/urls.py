from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name = 'my_index'),
	url(r'^survey/process$', views.process_users, name = 'my_process'),
	url(r'^result$', views.result_users, name = 'my_result' ),
	url(r'^reset$', views.reset, name = 'my_reset')
]