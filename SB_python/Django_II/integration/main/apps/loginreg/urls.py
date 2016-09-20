from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='loginreg_index'),
    url(r'^login$', views.login, name='loginreg_login'),
    url(r'^register$', views.register, name='loginreg_register'),
    url(r'^logoff$', views.logoff, name='loginreg_logoff')
]
