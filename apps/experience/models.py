from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist, ValidationError

LANGUAGES = (
    ('TR', 'Turkish'),
    ('EN', 'English'),
)


class Experience(models.Model):
    name = models.CharField(max_length=50,verbose_name="Company Name")
    position = models.CharField(max_length=150,verbose_name="Position")
    position_sector = models.CharField(max_length=200,verbose_name="Sector")
    #industry = models.ForeignKey(max_length=200,verbose_name="Industry")
    location = models.CharField(max_length=250, verbose_name="Location")
    start_date = models.DateField(null=True, blank=True, verbose_name=_("start date"))
    end_date = models.DateField(null=True, blank=True, verbose_name=_("end date"))
    description = models.TextField(default=None,null=True,blank=True, verbose_name=_("description"))
    link = models.URLField(blank=True,verbose_name="Company URL")
    #image = models.ImageField(upload_to="images", blank=True,null=True)
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