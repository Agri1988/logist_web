from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView

from . import models
from . import forms

class ServiceListView(ListView):
    template_name = 'services_app/service_list.html'
    model = models.Service


class ServiceCreateView(CreateView):
    template_name = 'services_app/detail_service.html'
    model = models.Service
    form_class = forms.ServiceForm


class ServiceUpdateView(UpdateView):
    template_name = 'services_app/detail_service.html'
    model = models.Service
    form_class = forms.ServiceForm