from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate, login
from caisse.models import Stock


def user(request):
    article = Stock
    return render(request, 'caisse/userPage.html', {'articles': article})


def accueil(request):
    return render(request, 'caisse/accueil.html')

