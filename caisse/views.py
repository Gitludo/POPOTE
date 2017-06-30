from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate, login
from caisse.models import Stock


def user(request):
    articles = Stock.objects.all()
    return render(request, 'caisse/userPage.html', {'articles': articles})


def accueil(request):
    return render(request, 'caisse/accueil.html')

