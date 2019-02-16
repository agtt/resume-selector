from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, BaseDetailView
from django.views.generic import ListView
from .models import *
from .forms import *


class ExperienceList(ListView):
    template_name = "experience/experience_list.html"
    #model = Experience

    def get_queryset(self):
        return Experience.objects.filter(user=self.request.user)


class ExperienceCreate(CreateView):
    template_name = "experience/experience_form.html"
    model = Experience
    form_class = ExperienceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ExperienceCreate, self).form_valid(form)


class ExperienceUpdate(UpdateView):
    model = Experience
    # fields = ['name']


class ExperienceDelete(DeleteView):
    model = Experience
    # fields = ['name']
