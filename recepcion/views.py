from django.shortcuts import render, redirect
from functools import wraps

def proteger_vista(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('autenticado'):
            return redirect('/')
        return func(request, *args, **kwargs)
    return wrapper
equipos_recibidos = []

@proteger_vista
def registrar_equipo(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        tipo_equipo = request.POST.get('tipo_equipo')
        problema = request.POST.get('problema')
        
        equipo = {
            'nombre_cliente': nombre_cliente,
            'tipo_equipo': tipo_equipo,
            'problema': problema,
            'id': len(equipos_recibidos) + 1
        }
        
        equipos_recibidos.append(equipo)
        
        return render(request, 'recepcion/registrar.html', {
            'mensaje_exito': f'Equipo de {nombre_cliente} registrado correctamente.'
        })
    
    return render(request, 'recepcion/registrar.html')

@proteger_vista
def listado_equipos(request):
    return render(request, 'recepcion/listado.html', {
        'equipos': equipos_recibidos
    })

@proteger_vista
def detalle_equipo(request, nombre):
    equipo = next((eq for eq in equipos_recibidos if eq['nombre_cliente'] == nombre), None)
    
    if equipo:
        return render(request, 'recepcion/detalle.html', {'equipo': equipo})
    else:
        return render(request, 'recepcion/detalle.html', {
            'mensaje_error': 'Equipo no encontrado.'
        })