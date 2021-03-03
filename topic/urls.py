from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.topics_list, name='topics_list'),
    # ex: /polls/5/
    path('<str:topic_title>/', views.topic_details, name='topic_details'),
    # # ex: /polls/5/results/
    path('<str:topic_title>/posts/', views.topic_posts, name='topic_posts'),

    path('<str:topic_title>/posts/<str:post_title>', views.post_details, name='post_details'),
    path('<str:topic_title>/posts/<str:post_title>/comments', views.post_comments, name='post_comments'),
    path('<str:topic_title>/posts/<str:post_title>/comments/<str:comment_title>', views.comment_details, name='comment_details'),
]