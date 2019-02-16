from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError


# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Education(AbstractBaseModel):
    name = models.CharField(max_length=250,verbose_name="School Name")
    degree = models.CharField(max_length=250,verbose_name="Degree")
    chapter = models.CharField(max_length=250,verbose_name="Chapter")
    link = models.URLField('School URL',blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    #is_current = models.BooleanField(default=False,blank=True,null=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education_user")

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