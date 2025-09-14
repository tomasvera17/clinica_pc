from django.shortcuts import render
from recepcion.views import proteger_vista
from diagnostico.views import diagnosticos_realizados
from datetime import datetime
import pytz

@proteger_vista
def verificar_estado(request):
    from recepcion.views import equipos_recibidos
    
    nombre_cliente = request.GET.get('nombre_cliente', '')
    equipo_encontrado = None
    diagnostico_encontrado = None
    
    if nombre_cliente:
        equipo_encontrado = next((eq for eq in equipos_recibidos if eq['nombre_cliente'] == nombre_cliente), None)
        
        if equipo_encontrado:
            diagnostico_encontrado = next((diag for diag in diagnosticos_realizados if diag['equipo']['id'] == equipo_encontrado['id']), None)
    
    return render(request, 'entrega/verificar.html', {
        'equipo': equipo_encontrado,
        'diagnostico': diagnostico_encontrado,
        'nombre_buscado': nombre_cliente
    })

@proteger_vista
def reporte_entrega(request):
    from recepcion.views import equipos_recibidos
    
    if request.method == 'POST':
        equipo_id = request.POST.get('equipo_id')
        estado_final = request.POST.get('estado_final')
        observaciones = request.POST.get('observaciones')
        
        for equipo in equipos_recibidos:
            if equipo['id'] == int(equipo_id):
                equipo['estado_final'] = estado_final
                equipo['observaciones'] = observaciones
                break
        
        return render(request, 'entrega/reporte.html', {
            'equipos': equipos_recibidos,
            'mensaje_exito': 'Estado de entrega registrado correctamente.'
        })
    
    return render(request, 'entrega/reporte.html', {
        'equipos': equipos_recibidos
    })

@proteger_vista
def comprobante_entrega(request):
    from recepcion.views import equipos_recibidos
    
    nombre_cliente = request.GET.get('nombre_cliente', '')
    equipo_encontrado = None
    diagnostico_encontrado = None
    
    chile_tz = pytz.timezone('Chile/Continental')
    fecha_chile = datetime.now(chile_tz)
    fecha_formateada = fecha_chile.strftime("%d/%m/%Y %H:%M")
    
    if nombre_cliente:
        equipo_encontrado = next((eq for eq in equipos_recibidos if eq['nombre_cliente'] == nombre_cliente), None)
        
        if equipo_encontrado:
            diagnostico_encontrado = next((diag for diag in diagnosticos_realizados if diag['equipo']['id'] == equipo_encontrado['id']), None)
    
    return render(request, 'entrega/comprobante.html', {
        'equipo': equipo_encontrado,
        'diagnostico': diagnostico_encontrado,
        'nombre_buscado': nombre_cliente,
        'fecha_actual': fecha_formateada 
    })