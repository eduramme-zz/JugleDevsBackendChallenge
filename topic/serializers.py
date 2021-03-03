from django.contrib.auth.models import Topic
from rest_framework import serializers


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'title', 'description', 'URLName', 'created_at', 'updated_at']
