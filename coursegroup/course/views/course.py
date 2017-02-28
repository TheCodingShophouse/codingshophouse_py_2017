from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from course.models import Course
from django.urls import reverse_lazy


class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course
    
class CourseCreateView(CreateView):
    model = Course
    fields = ["title", "description", "instructor"]
    success_url = reverse_lazy("course-list")


class CourseEditView(UpdateView):
    model = Course
    fields = ["title", "description", "instructor"]
    success_url = reverse_lazy("course-list")


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course-list")
    
