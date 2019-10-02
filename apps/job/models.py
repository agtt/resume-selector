from django.db import models
from django.contrib.auth.models import User


class Industry(models.Model):
    name = models.CharField(max_length=250, verbose_name="Inudstry Name", blank=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=250, verbose_name="Section Name", blank=True)

    def __str__(self):
        return self.name


JOB_TYPE = (
    (1, 'Full-Time'),
    (2, 'Part-Time'),
    (3, 'Contract'),
    (4, 'Temporary'),
    (99, 'Other'),
)


class Job(models.Model):
    name = models.CharField(max_length=250, verbose_name="Name", blank=True)
    type = models.IntegerField(choices=JOB_TYPE, default=99)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="job_industry", blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="job_section", blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_user")

    def __str__(self):
        return self.name
