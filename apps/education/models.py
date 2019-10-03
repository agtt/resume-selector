from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError


class University(models.Model):
    name = models.CharField(max_length=250, verbose_name="University Name")
    image = models.ImageField(blank=True, null=True, verbose_name="Logo")

    def __str__(self):
        return self.name


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Education(AbstractBaseModel):
    name = models.CharField(max_length=250, verbose_name="School Name", null=True, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="education_university",
                                   blank=True, null=True)
    degree = models.CharField(max_length=250, verbose_name="Degree",blank=True)
    chapter = models.CharField(max_length=250, verbose_name="Chapter", blank=True)
    grade = models.CharField(max_length=250, verbose_name="Grade",blank=True)
    link = models.URLField('School URL', blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField(blank=True, null=True, default=False)
    description = models.TextField(blank=True)
    activities = models.TextField(blank=True, verbose_name="Activities and Societies")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education_user")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.clean()
        return super(self.__class__, self).save(*args, **kwargs)

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError({"start_date": _("Start date must be "
                                                       "before end date."),
                                       "end_date": _("Start date must be "
                                                     "before end date.")})

    def get_absolute_url(self):
        return "/apps/education/"
