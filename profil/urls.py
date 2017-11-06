from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns= [
    url(r'^$', views.dire_bonjour, name='dire_bonjour'),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion')
   
    
]