from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^1$', views.one, name = 'index'),
    url(r'^2$', views.two),
    url(r'^3$', views.three),
    url(r'^4$', views.four),
    url(r'^5$', views.five),
    url(r'^6$', views.six),
    url(r'^7$', views.seven),
    url(r'^8$', views.eight)
]
