from django.conf.urls import url
from course.views import TopicListView
from course.views import TopicCreateView
from course.views import TopicEditView
from course.views import TopicDetailView
from course.views import file_upload


urlpatterns = [
    url(r'^home', file_upload.home, name='home'),
    url(r'^upload_simple/$', file_upload.simple_upload, name='simple_upload'),
    url(r'^upload_model/$', file_upload.model_form_upload, name='model_form_upload'),

    url(r"^create$", TopicCreateView.as_view(), name="topic-create"),
    url(r"^edit/(?P<pk>\d+)$", TopicEditView.as_view(), name="topic-edit"),
    url(r"^(?P<topic_id>\d+)$", TopicDetailView.as_view(), name="topic-detail"),
    url(r"^$", TopicListView.as_view(), name="topic-list"),
]




