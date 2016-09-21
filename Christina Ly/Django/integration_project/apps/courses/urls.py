from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'my_index'),
    url(r'^integration$', views.integration, name = 'my_integration'),
    url(r'^courses$', views.courses, name = 'my_courses'),
    url(r'^destroy/(?P<id>\d+)$', views.destroyconfirm, name = 'my_destroy'),
    url(r'^deleted$', views.destroy, name = 'my_deleted'),
    url(r'^form$', views.form, name ="my_form")
]