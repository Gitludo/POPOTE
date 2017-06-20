from django.shortcuts import render
from django.http import Http404

def user(request):
    return render(request, 'caisse/user.html')

def accueil(request):
    return render(request, 'caisse/accueil.html')
