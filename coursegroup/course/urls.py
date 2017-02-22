from django.conf.urls import url
from course.views import TopicListView
from course.views import TopicView
from course.views import TopicCreateView
from course.views import TopicEditView

urlpatterns = [
    url(r"^create$", TopicCreateView.as_view(), name="topic-create"),
    url(r"^edit/(?P<topic_id>\d+)$", TopicEditView.as_view(), name="topic-edit"),
    url(r"^$", TopicListView.as_view(), name="topic-list"),
]