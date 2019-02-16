from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *


class EducationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EducationForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = User.objects.all()


    class Meta:
        model = Education
        fields = '__all__'
        exclude = ('user','is_current',)
