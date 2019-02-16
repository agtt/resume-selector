from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, BaseDetailView
from django.views.generic import ListView
from .models import *
from .forms import *


class EducationList(ListView):
    template_name = "education/education_list.html"
    model = Education


    def get_queryset(self):
        return Education.objects.filter(user=self.request.user)


class EducationCreate(CreateView):
    template_name = "education/education_form.html"
    model = Education
    form_class = EducationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationCreate, self).form_valid(form)


class EducationUpdate(UpdateView):
    model = Education
    # fields = ['name']


class ExperienceDelete(DeleteView):
    model = Education
    # fields = ['name']
