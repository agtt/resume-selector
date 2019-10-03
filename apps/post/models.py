from django.db import models
from django.contrib.auth.models import User


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Comment(AbstractBaseModel):
    name = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Like(AbstractBaseModel):
    point = models.IntegerField(default=1, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")

    def __str__(self):
        return self.point


class Post(AbstractBaseModel):
    name = models.TextField(blank=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name="post_comments")
    likes = models.ManyToManyField(Like, blank=True, related_name="post_likes")
    total_like = models.IntegerField(default=0, blank=True)
    total_dislike = models.IntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")

    def __str__(self):
        return self.name
