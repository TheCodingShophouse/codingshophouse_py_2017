from django.conf.urls import url

from . import views
from course import views
from course.views import file_upload

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home', file_upload.home, name='home'),
    url(r'^upload_simple/$', file_upload.simple_upload, name='simple_upload'),
    url(r'^upload_model/$', file_upload.model_form_upload, name='model_form_upload'),
]