from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serialazers import PartnerSerialazer
from ..models import Partner



# Create your views here.

class PartnerViewSet(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerialazer

    def get_queryset(self):
        my_firm = self.request.query_params.get('my_firm', None)
        if my_firm is not None:
            queryset = Partner.objects.filter(is_self_firm=my_firm)
            #print(queryset)
        else:
            queryset = Partner.objects.all()
        return queryset



