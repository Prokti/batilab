from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Chantier, CalculeMaison
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class ListeChantier(ListView):
    
    model = Chantier
    context_object_name = 'derniers_chantiers'
    template_name = 'chantiers/liste_chantiers.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):        
        return super(ListeChantier, self).dispatch(request, *args, **kwargs)

class DetailChantier(DetailView):
    context_object_name = "chantier"
    template_name = "chantiers/detail.html"
    model = Chantier



class CalculeMaison(DetailView):
    context_object_name = "calcule"
    template_name = 'chantiers/calcules.html'
    model = CalculeMaison