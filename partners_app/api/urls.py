from rest_framework import routers
from django.conf.urls import include
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register('partner', views.PartnerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('clients_list', views.ClientViewSet.as_view({'get':'list'}), name='clients_list_api' ),

]

