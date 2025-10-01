from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_process(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Credenciales incorrectas.')
            return redirect('login')
