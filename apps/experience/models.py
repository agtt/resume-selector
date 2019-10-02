from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from apps.company.models import Company
from apps.job.models import Industry


class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="experience_company", blank=True)
    position = models.CharField(max_length=150, verbose_name="Position")
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="experience_industry", blank=True)
    location = models.CharField(max_length=250, verbose_name="Location", blank=True)
    start_date = models.DateField(null=True, blank=True, verbose_name=_("start date"))
    end_date = models.DateField(null=True, blank=True, verbose_name=_("end date"))
    description = models.TextField(default=None, null=True, blank=True, verbose_name=_("description"))
    link = models.URLField(blank=True, verbose_name="Company URL", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experience_user")

    def __repr__(self):
        return '<Experience: %s>' % self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-end_date']

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
        return "/apps/experience/"
