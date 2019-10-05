from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE)
    read = models.IntegerField(default=0)
    receiver = models.ForeignKey(User, related_name='message_receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
