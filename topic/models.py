from django.db import models

# class Question(models.Model):
#   questin_text = models.Charfield(max_length = 300)

class Topic(models.Model):
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
