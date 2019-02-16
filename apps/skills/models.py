from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError

class Skills(models.Model):
    name = models.CharField(max_length=250,verbose_name="Skill Name")