from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100)
    URLName = models.SlugField(max_length = 100)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')