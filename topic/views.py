from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic
from post.models import Post
from comment.models import Comment


def topics_list(request):
    topics_list = Topic.objects.order_by('-created_at')
    output = ', '.join([q.title for q in topics_list])
    return HttpResponse(output)

def topic_details(request, topic_title):
    try:
      topic = Topic.objects.get(title=topic_title)
      try:
        topics = Post.objects.filter(topic=topic)[:5]
        topic_text = ', '.join([q.title for q in topics])
      except:
        topic_text = 'no posts'
      return HttpResponse("topic: %s | posts: %s" % (topic.title, topic_text))
    except:
      return HttpResponse("No topics with that title")


def topic_posts(request, topic_title):
    try:
      topic = Topic.objects.get(title=topic_title)
      try:
        posts = Post.objects.filter(topic=topic)
        posts_text = ', '.join([q.title for q in posts])
      except:
        posts_text = 'no posts'
      return HttpResponse("posts: %s" % (posts_text))
    except:
      return HttpResponse("No topics with that title")

def post_details(request, topic_title, post_title):
    try:
      topic = Topic.objects.get(title=topic_title)
      try:
        post = Post.objects.get(title=post_title)
        try:
          comments = Comment.objects.filter(post=post)[:5]
          comments_text = ', '.join([q.content for q in comments])
        except:
          comments_text = 'no comments'
        posts_text = f'title: {post.title} | description: {post.content} | comments: {comments_text}'
        return HttpResponse(posts_text)
      except:
        posts_text = "post doesn't exist"
      return HttpResponse("posts: %s" % (posts_text))
    except:
      return HttpResponse("No topics with that title")
    return HttpResponse("lists details and some comments from a post), topic %s, post %s" % (topic_id, post_id))

def post_comments(request, topic_title, post_title):
    try:
      topic = Topic.objects.get(title=topic_title)
      try:
        post = Post.objects.get(title=post_title)
        try:
          comments = Comment.objects.filter(post=post)
          comments_text = ', '.join([q.title for q in comments])
        except:
          comments_text = 'no comments'
        posts_text = f'comments: {comments_text}'
      except:
        posts_text = "post doesn't exist"
      return HttpResponse("posts: %s" % (posts_text))
    except:
      return HttpResponse("No topics with that title")
    return HttpResponse("lists details and some comments from a post), topic %s, post %s" % (topic_id, post_id))
    
def comment_details(request, topic_title, post_title, comment_title):
    try:
      topic = Topic.objects.get(title=topic_title)
      try:
        post = Post.objects.get(title=post_title)
        try:
          comment = Comment.objects.get(title=comment_title)
          comment_text = f'comment: {comment.content}'
        except:
          comment_text = 'comment not found'
        return HttpResponse(comment_text)
      except:
        posts_text = "post doesn't exist"
      return HttpResponse("posts: %s" % (posts_text))
    except:
      return HttpResponse("No topics with that title")
    return HttpResponse("lists details and some comments from a post), topic %s, post %s" % (topic_id, post_id))