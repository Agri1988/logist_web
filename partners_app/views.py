from django.shortcuts import render
from django.views.generic import ListView
from .models import Partner
from django.template.loader import render_to_string, get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from .forms import PartnerForm


class PartnerListView(ListView):
    template_name = 'partners_app/partner_list.html'
    queryset = Partner.objects.all()
    context_object_name = 'partners'


