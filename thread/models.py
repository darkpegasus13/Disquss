from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_title = models.CharField(max_length=80)
    category = models.CharField(max_length=50)
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)


class Post_reply(models.Model):
    post = models.CharField(max_length=500)
    question = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="reply_likes", blank=True)
    Post_reply_reply = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='nested_comments')

