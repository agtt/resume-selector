from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=250, verbose_name="Language")
    level = models.IntegerField(
        choices=((1, 1), (2, 1.5), (3, 2), (4, 2.5), (5, 3), (6, 3.5), (7, 4), (8, 4.5), (9, 5)),
        default=1, verbose_name="Proficiency",blank=True)

    def __str__(self):
        return self.name
