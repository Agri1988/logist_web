from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serialazers import ServiceSerialazer
from ..models import Service



# Create your views here.

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerialazer


