from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'integration_index'),
    url(r'^merge$', views.merge, name = 'integration_merge')
]