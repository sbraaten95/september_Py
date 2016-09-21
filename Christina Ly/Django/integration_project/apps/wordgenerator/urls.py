from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^word$', views.create, name = 'my_word'),
    url(r'^reset$', views.reset, name ='my_resetmy_')
]
