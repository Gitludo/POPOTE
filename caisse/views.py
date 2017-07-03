from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from caisse.models import Stock
from caisse.forms import ConnexionForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required
def user(request):
    articles = Stock.objects.all()
    return render(request, 'caisse/userPage.html', {'articles': articles})


def accueil(request):
    return render(request, 'caisse/accueil.html')

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'caisse/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(accueil))

