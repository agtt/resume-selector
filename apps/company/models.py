from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=250,verbose_name="Company Name")
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True,verbose_name="Logo")

    def __str__(self):
        return self.name
