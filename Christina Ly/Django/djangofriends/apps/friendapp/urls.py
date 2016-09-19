from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^filter$', views.filterlast),
    url(r'^exclude$', views.excludelast),
    url(r'^chain$', views.chaining),
    url(r'^madison$', views.madison),
    url(r'^danmike$', views.danmike),
    url(r'^getrodriguez$', views.getrodriguez),
    url(r'^thousand$', views.getthousand),
    url(r'^orderfirst$', views.orderfirst),
    url(r'^orderreverse$', views.orderreverse),
    url(r'^allobjects$', views.all),
    url(r'^friendship4table$', views.friendship4table),
    url(r'^frienduser4$', views.frienduser4),
    url(r'^friendnot$', views.friendnot)
]
