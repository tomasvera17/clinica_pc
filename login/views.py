from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm

def vista_login(request):
    mensaje_error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Usar el sistema de autenticación de Django
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            # Redirigir según el tipo de usuario si es necesario
            return redirect('recepcion:registrar_equipo')
        else:
            mensaje_error = "Credenciales incorrectas. Intente nuevamente."
    
    return render(request, 'login/login.html', {'mensaje_error': mensaje_error})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required
def registro_usuario(request):
    """Vista para registrar nuevos usuarios (solo accesible para administradores)"""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado exitosamente.')
            return redirect('vista_login')  # Cambia por tu vista de destino
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'login/registro_usuario.html', {'form': form})