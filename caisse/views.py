from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate, login


def user(request):
    return render(request, 'caisse/user.html', locals())


def accueil(request):

    return render(request, 'caisse/accueil.html')



def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'caisse/user.html')
    else:
        return Http404

