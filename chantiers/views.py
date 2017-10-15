from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Chantier
from django.contrib.auth.decorators import login_required


# Create your views here.


class ListeChantier(ListView):
    model = Chantier
    context_object_name = 'derniers_chantiers'
    template_name = 'chantiers/liste_chantiers.html'

class DetailChantier(DetailView):
    context_object_name = "chantier"
    template_name = "chantiers/detail.html"
    model = Chantier


