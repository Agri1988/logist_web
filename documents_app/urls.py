from django.conf.urls import url
from django.urls import path, include
from . import views

from . import views

from . import views
import datetime
app_name = 'documents_app'
urlpatterns = [
    path('', views.DocumentListView.as_view(), name='all_documents'),
    path('api/', include('documents_app.api.urls')),
    path('create/', views.DocumentCreateView.as_view(), name='document_create'),
    path('edit/<int:pk>/', views.DocumentUpdateView.as_view(), name='document_update'),
    path('save_document/', views.DocumentSave.as_view(), name='document_saave'),

]