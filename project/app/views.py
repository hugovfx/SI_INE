from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request, "index.html")

def logout_view(request):
    logout(request)
    return redirect('index')

def privacy(request):
    return render(request, 'aviso-privacidad.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html' )