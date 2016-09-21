from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^validate_register$', views.register, name ='my_register'),
    url(r'^validate_login$', views.login, name = 'my_login'),
    url(r'^books$', views.home, name = 'books_home'),
    url(r'^users/(?P<id>\d+)$', views.reviewer, name ="reviewer"),
    url(r'^logout$', views.logout, name = 'logout')
]