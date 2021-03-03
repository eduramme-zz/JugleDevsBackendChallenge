from django.db import models
import django
from post.models import Post

class Comment(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)