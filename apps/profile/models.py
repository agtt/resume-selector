from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from apps.language.models import Language
from apps.skill.models import Skill
from apps.job.models import Industry

GENDER = (('man', 'Man'), ('woman', 'Woman'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name="profile", verbose_name=_('User'),
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name="Name", blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="profile_industry", blank=True,
                                 null=True)
    description = models.TextField(default=None, null=True, blank=True, verbose_name=_("Description"))
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Phone'))
    gender = models.CharField(max_length=40, blank=True, verbose_name=_('Gender'), choices=GENDER)
    background = models.ImageField(upload_to='userprofiles2/background', blank=True, null=True,
                                   verbose_name=_('Background'))
    avatar = models.ImageField(upload_to='userprofiles2/avatars', blank=True, null=True, verbose_name=_('Photo'))
    completion_level = models.PositiveSmallIntegerField(default=0, verbose_name=_('Profile completion percentage'))
    email_is_verified = models.BooleanField(default=False, verbose_name=_('Email is verified'))
    personal_info_is_completed = models.BooleanField(default=False, verbose_name=_('Personal info completed'))
    languages = models.ManyToManyField(Language, blank=True, related_name="profile_languages")
    skills = models.ManyToManyField(Skill, blank=True, related_name="profile_skills")

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return "User profile: %s" % self.user.username

    def get_completion_level(self):
        completion_level = 0
        if self.email_is_verified:
            completion_level += 50
        if self.personal_info_is_completed:
            completion_level += 50
        return completion_level

    def update_completion_level(self):
        self.completion_level = self.get_completion_level()
        self.save()
