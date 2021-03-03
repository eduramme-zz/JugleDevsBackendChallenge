"""
Accounts URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include

from django.contrib import admin
from django.urls import include, path


###
# URL Patterns
###
urlpatterns = [
    path('user/', include('User.urls')),
    url(r'^api/v1/', include('accounts.api.v1.urls'))
]
