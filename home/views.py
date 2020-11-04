from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handlelogout(request):
    if request.method == "POST":
        logout(request)
    else:
        pass
    return redirect('home')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            print('user is present')
            login(request, user)
        else:
            print('no user found.')
    else:
        pass
    return redirect('home')