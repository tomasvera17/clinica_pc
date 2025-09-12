from django.shortcuts import render, redirect

def vista_login(request):
    mensaje_error = None
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')
        
        if usuario == 'inacap' and clave == 'clinica2025':
            request.session['autenticado'] = True
            request.session.set_expiry(3600)
            return redirect('/recepcion/registrar/')
        else:
            mensaje_error = "Credenciales incorrectas. Intente nuevamente."
    
    return render(request, 'login/login.html', {'mensaje_error': mensaje_error})

def cerrar_sesion(request):
    if 'autenticado' in request.session:
        del request.session['autenticado']
    return redirect('/')
