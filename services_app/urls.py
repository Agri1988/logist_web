from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView

from . import views

from . import views
import datetime
app_name = 'services_app'
urlpatterns = [
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('api/', include('services_app.api.urls')),
    path('create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('edit/<int:pk>/', views.ServiceUpdateView.as_view(), name='service_update'),
]