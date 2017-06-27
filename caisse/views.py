from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate, login


def user(request):
    return render(request, 'caisse//userCaisse.html', locals())


def accueil(request):
    return render(request, 'caisse/accueil.html')
