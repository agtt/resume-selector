from django.db import models
from django.contrib.auth.models import User


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(AbstractBaseModel):
    content = models.TextField(blank=True)
    total_like = models.IntegerField(default=0, blank=True)
    total_dislike = models.IntegerField(default=0, blank=True)
    score = models.IntegerField(default=0, blank=True)
    image = models.ImageField(upload_to='userprofiles2/posts', blank=True, verbose_name="Image")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")

    def __str__(self):
        return self.content


class Like(AbstractBaseModel):
    point = models.IntegerField(choices=((1, 1), (-1, -1)), blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="like_user")

    def __str__(self):
        return str(self.point)


class Comment(AbstractBaseModel):
    content = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")

    def __str__(self):
        return self.content
