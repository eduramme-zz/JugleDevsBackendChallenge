"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from helpers.health_check_view import health_check

# from django.urls import include, paths
from rest_framework import routers
from User import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('accounts.urls')),
    url('topics/', include('topic.urls')),
]
