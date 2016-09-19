from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^1$', views.one, name = 'index'),
    url(r'^2$', views.two),
    url(r'^3$', views.three)
]
