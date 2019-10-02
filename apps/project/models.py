from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    name = models.CharField(max_length=300,verbose_name="Title")
    description = models.TextField(blank=True,verbose_name="Description")
    summary = models.TextField(blank=True,verbose_name="Summary")
    start_date = models.DateField(null=True, blank=True, verbose_name=_("Start Date"))
    end_date = models.DateField(null=True, blank=True, verbose_name=_("End Date"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_user")
