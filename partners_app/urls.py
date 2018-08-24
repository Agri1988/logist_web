from django.conf.urls import url
from django.urls import path, include
from . import views

from . import views
import datetime
app_name = 'partners_app'
urlpatterns = [
    path('', views.PartnerListView.as_view(), name='all_partners'),
    path('api/', include('partners_app.api.urls'))

]