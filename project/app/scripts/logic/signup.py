from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

def signup(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_completo').strip()
        curp = request.POST.get('curp').strip().upper()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        User = get_user_model()

        if password != confirm:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('signup')

        try:
            validate_password(password)
        except ValidationError as e:
            for error in e:
                messages.error(request, error)
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado.')
            return redirect('signup')

        if User.objects.filter(curp=curp).exists():
            messages.error(request, 'Esta CURP ya está registrada.')
            return redirect('signup')

        User.objects.create_user(
            email=email,
            password=password,
            nombre_completo=nombre,
            curp=curp,
        )

        messages.success(request, 'Registro exitoso. Ahora inicia sesión.')
        return redirect('login')
