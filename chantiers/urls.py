from django.conf.urls import  url, include
from django.views.generic import ListView
from . import views
from .models import Chantier

urlpatterns =[
    url(r'^$', views.ListeChantier.as_view(), name ="chantier_liste"),
    url(r'^chantier/(?P<pk>\d+)$', views.DetailChantier.as_view(), name ='chantier_detail'),
    url(r'^calcules/(?P<pk>\d+)$', views.CalculeMaison.as_view(), name="calcule_maison"),
    
]