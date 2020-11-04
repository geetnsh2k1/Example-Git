from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')