from rest_framework import serializers

from ..models import Document
from services_app.api.serialazers import ServiceSerialazer
from partners_app.api.serialazers import PartnerSerialazer

class DocumentSerialazer(serializers.ModelSerializer):
    services_obj = ServiceSerialazer(source='services', many=True, read_only=True)
    partner_obj =  PartnerSerialazer(source='partner', read_only=True)
    class Meta:
        model = Document
        fields = '__all__'