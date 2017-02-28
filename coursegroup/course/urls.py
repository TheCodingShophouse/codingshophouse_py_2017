from django.conf.urls import url
from course.views import *
from course.views import file_upload

urlpatterns = [
    url(r'^home', file_upload.home, name='home'),
    url(r'^upload_simple/$', file_upload.simple_upload, name='simple_upload'),
    url(r'^upload_model/$', file_upload.model_form_upload, name='model_form_upload'),

    url(r"^topic/create$", TopicCreateView.as_view(), name="topic-create"),
    url(r"^topic/edit/(?P<topic_id>\d+)$", TopicEditView.as_view(), name="topic-edit"),
    url(r"^topic/(?P<topic_id>\d+)$", TopicDetailView.as_view(), name="topic-detail"),
    url(r"^topic$", TopicListView.as_view(), name="topic-list"),

    url(r"^course/create$", CourseCreateView.as_view(), name="course-create"),
    url(r"^course/edit/(?P<topic_id>\d+)$", CourseEditView.as_view(), name="course-edit"),
    url(r"^(?P<course_id>\d+)$", CourseDetailView.as_view(), name="course-detail"),
    url(r"^course$", CourseListView.as_view(), name="course-list"),
]




