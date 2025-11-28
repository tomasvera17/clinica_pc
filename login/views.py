from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm

@login_required
def dashboard(request):
    from recepcion.models import Equipo
    from diagnostico.models import Diagnostico
    from entrega.models import Entrega
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    context = {
        'equipos_count': Equipo.objects.count(),
        'diagnosticos_pendientes_count': Diagnostico.objects.filter(descripcion_diagnostico='').count(),
        'entregas_count': Entrega.objects.count(),
        'tecnicos_count': User.objects.filter(tipo_usuario='tecnico').count(),
        'ultimos_equipos': Equipo.objects.all().order_by('-fecha_recepcion')[:5]
    }
    
    return render(request, 'dashboard.html', context)

def vista_login(request):
    mensaje_error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}!')
            # Redirección final al dashboard
            return redirect('login:dashboard')  # ← Esta es la correcta
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
