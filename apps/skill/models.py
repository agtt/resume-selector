from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=250, verbose_name="Skill Name")

    def __str__(self):
        return self.name
