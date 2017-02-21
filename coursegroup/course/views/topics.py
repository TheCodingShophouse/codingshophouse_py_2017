from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views import View
from django.shortcuts import render
from django.http import Http404
from course.models import Topic
from course.models import Discussion


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

#this is discussion.py
#discussion has foreign key to main topic
#discussion also manage discussion
#it must have text field
#post will create new discussion
#get will list all discussion
#topic.discussions.all

class TopicDetailView (View):

    def get(self, requests, topic_id):
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            raise Http404("Does Not Exist")
        discussions = topic.discussions.all()
        return render(requests, "topic_detail.html", {"topic": topic, "discussion": discussions})

    def post(self, requests, topic_id):
        form_data = requests.POST
        try:
            topic = Topic.objects.get(id=topic_id)
        except Topic.DoesNotExist:
            raise Http404("Does Not Exist")
        discussion = Discussion()
        discussion.content = form_data.get("content")
        discussion.topic = topic
        discussion.save() discussions = topic.discussions.all()
        return redirect("topic-edit", topic_id=topic.id)

