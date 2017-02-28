from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from course.models import Course
from django.urls import reverse_lazy


class TopicListView(ListView):
    model = Course

class CourseView(DetailView):
    model = Course
    
class TopicCreateView(CreateView):
    model = Course
    fields = ["title", "description"]
    success_url = reverse_lazy("course-list")


class TopicEditView(UpdateView):
    model = Course
    fields = ["title", "description"]
    success_url = reverse_lazy("course-list")


class TopicDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course-list")
    
