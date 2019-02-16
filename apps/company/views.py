from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, BaseDetailView
from django.views.generic import ListView
from .models import *


def company_list(request):
    return render(request,'company/company_list.html',{})
