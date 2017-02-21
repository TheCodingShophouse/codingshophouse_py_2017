from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class TopicListView(ListView):
    model = TopicListPost

class TopicCreateView(CreateView):
    model = TopicPost
    fields = ["title", "content"]


class TopicEditView(UpdateView):
    model = TopicPost
    fields = ["title", "content"]


class TopicDeleteView(DeleteView):
    model = TopicPost
    success_url = reverse_lazy("topic-list")