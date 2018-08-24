from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views



from . import views

app_name = 'base_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='base_app/index.html'), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login_'),
    path('auth/', include('django.contrib.auth.urls')),
]
