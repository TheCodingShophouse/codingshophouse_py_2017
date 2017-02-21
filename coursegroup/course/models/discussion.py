from django.db import models
from .topic import Topic

class Discussion (models.Model):

      topic = models.ForeignKey(Topic)
      content = models.TextField()
