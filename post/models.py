from django.db import models
from topic.models import Topic

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)