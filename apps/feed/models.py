from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    pass


class Like(models.Model):
    pass


class Post(models.Model):
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feed_user")