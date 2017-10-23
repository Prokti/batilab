
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse
from .forms import ConnexionForm
from django.http import HttpResponse

def connexion(request):
    

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('chantier_liste')
                           
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))



def dire_bonjour(request):
    if request.user.is_authenticated():
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut, anonyme.")


def connex(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        return redirect('https://berdin.immo')
    

