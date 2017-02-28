from django.db import models
from .course import Course

class Topic(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    course = models.ForeignKey(Course, null = True) 