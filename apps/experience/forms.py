from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *


class ExperienceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExperienceForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = User.objects.all()


    # def save(self, *args, **kwargs):
    #     # kwargs['commit'] = False
    #     print("aaaaaaaaaaaaaaaaaaaaaaaaa")
    #     obj = super(ExperienceForm, self).save(*args, **kwargs)
    #     if self.request:
    #         obj.user = self.request.user
    #     obj.save()


    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ('user','image',)
