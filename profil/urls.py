from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


urlpatterns= [
    url(r'^connexion$', auth_views.login, {'template_name' : 'connexion.html'}),
    url(r'^deconnexion$', auth_views.logout, {'next_page': 'https://berdin.immo'}),
]