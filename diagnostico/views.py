from django.shortcuts import render, redirect
from recepcion.views import proteger_vista

diagnosticos_realizados = []

@proteger_vista
def asignar_diagnostico(request):
    from recepcion.views import equipos_recibidos
    
    equipos_asignados_ids = [diag['equipo']['id'] for diag in diagnosticos_realizados]
    
    equipos_disponibles = [eq for eq in equipos_recibidos if eq['id'] not in equipos_asignados_ids]
    
    if request.method == 'GET':
        estudiante = request.GET.get('estudiante')
        equipo_id = request.GET.get('equipo_id')
        
        if estudiante and equipo_id:
            equipo = next((eq for eq in equipos_recibidos if eq['id'] == int(equipo_id)), None)
            
            if equipo:
                diagnostico = {
                    'estudiante': estudiante,
                    'equipo': equipo,
                    'diagnostico': '',
                    'solucion': '',
                    'tipo_solucion': ''
                }
                
                diagnosticos_realizados.append(diagnostico)
                
                equipos_asignados_ids = [diag['equipo']['id'] for diag in diagnosticos_realizados]
                equipos_disponibles = [eq for eq in equipos_recibidos if eq['id'] not in equipos_asignados_ids]
                
                return render(request, 'diagnostico/asignar.html', {
                    'equipos': equipos_disponibles,
                    'diagnosticos_realizados': diagnosticos_realizados, 
                    'mensaje_exito': f'Equipo de {equipo["nombre_cliente"]} asignado a {estudiante} correctamente.'
                })
    
    return render(request, 'diagnostico/asignar.html', {
        'equipos': equipos_disponibles,
        'diagnosticos_realizados': diagnosticos_realizados 
    })

@proteger_vista
def evaluar_diagnostico(request):
    equipos_asignados_sin_diagnostico = []
    for diag in diagnosticos_realizados:
        if not diag['diagnostico']: 
            equipos_asignados_sin_diagnostico.append(diag['equipo'])
    
    if request.method == 'POST':
        equipo_id = request.POST.get('equipo_id')
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        tipo_solucion = request.POST.get('tipo_solucion')
        
        equipo_asignado = False
        for diag in diagnosticos_realizados:
            if diag['equipo']['id'] == int(equipo_id):
                equipo_asignado = True
                diag['diagnostico'] = diagnostico
                diag['solucion'] = solucion
                diag['tipo_solucion'] = tipo_solucion
                break
        
        if not equipo_asignado:
            return render(request, 'diagnostico/evaluar.html', {
                'equipos': equipos_asignados_sin_diagnostico,
                'mensaje_error': 'Error: El equipo seleccionado no está asignado.'
            })
        
        equipos_asignados_sin_diagnostico = [diag['equipo'] for diag in diagnosticos_realizados if not diag['diagnostico']]
        
        return render(request, 'diagnostico/evaluar.html', {
            'equipos': equipos_asignados_sin_diagnostico,
            'mensaje_exito': 'Diagnóstico registrado correctamente.'
        })
    
    return render(request, 'diagnostico/evaluar.html', {
        'equipos': equipos_asignados_sin_diagnostico
    })

@proteger_vista
def listado_diagnosticos(request):
    return render(request, 'diagnostico/listado.html', {
        'diagnosticos': diagnosticos_realizados
    })