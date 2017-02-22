from django.conf.urls import url
from course.views import TopicDetailView


urlpatterns = [
    url(r"^(?P<topic_id>\d+)$", TopicDetailView.as_view(), name="topic-detail"),
]


