from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=250, verbose_name="Language")

    def __str__(self):
        return self.name
