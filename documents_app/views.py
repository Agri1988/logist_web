from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView
from .models import Document
from services_app.models import Service
from .forms import DocumentForm

class DocumentListView(ListView):
    template_name = 'documents_app/document_list.html'
    model = Document



class DocumentCreateView(CreateView):
    template_name = 'documents_app/detail_document.html'
    model = Document
    form_class = DocumentForm


class DocumentUpdateView(UpdateView):
    template_name = 'documents_app/detail_document.html'
    model = Document
    form_class = DocumentForm

    def get_context_data(self, **kwargs):
        context = super(DocumentUpdateView, self).get_context_data(**kwargs)
        #print(context['form'].instance.services.all())
        context.update({'services':context['form'].instance.services.all()})
        print(context)
        # self.request.GET
        return context

class DocumentSave(View):
    def post(self, *args, **kwargs):
        
        return HttpResponse('all rigth')