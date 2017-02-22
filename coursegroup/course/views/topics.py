from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from course.models import Topic

class TopicListView(ListView):
    model = Topic

class TopicCreateView(CreateView):
    model = Topic
    fields = ["title", "content"]


class TopicEditView(UpdateView):
    model = Topic
    fields = ["title", "content"]


class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy("topic-list")