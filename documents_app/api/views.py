from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serialazers import DocumentSerialazer
from ..models import Document



# Create your views here.

class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerialazer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = (
        'id',
    )
    search_fields = (
    )

    def get_queryset(self):
        partner = self.request.query_params.get('partner', None)
        if partner is not None:
            queryset = Document.objects.filter(partner_id=partner)
            #print(queryset)
        else:
            queryset = Document.objects.all()

        return queryset



