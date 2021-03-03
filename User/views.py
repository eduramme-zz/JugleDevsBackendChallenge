from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import User
from rest_framework import viewsets
from rest_framework import permissions
from User.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

