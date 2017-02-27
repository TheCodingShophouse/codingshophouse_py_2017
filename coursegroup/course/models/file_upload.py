from __future__ import unicode_literals

from django.db import models
from .topic import Topic


class Document(models.Model):
    topic = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)