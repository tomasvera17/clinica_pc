from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from recepcion.models import Equipo
from .models import Diagnostico
from .forms import DiagnosticoForm

@login_required
def asignar_diagnostico(request):
    # Equipos que están en estado "recibido" y no tienen diagnóstico asignado
    equipos_sin_diagnostico = Equipo.objects.filter(
        estado='recibido'
    ).exclude(
        diagnostico__isnull=False
    )
    
    # Diagnosticos pendientes (asignados pero sin completar)
    diagnosticos_pendientes = Diagnostico.objects.filter(
        descripcion_diagnostico=''
    )
    
    if request.method == 'POST':
        equipo_id = request.POST.get('equipo')
        
        if equipo_id:
            equipo = get_object_or_404(Equipo, id=equipo_id, estado='recibido')
            
            # Crear diagnóstico asignado al usuario actual
            diagnostico = Diagnostico(
                equipo=equipo,
                tecnico=request.user,
                descripcion_diagnostico='',  # Vacío hasta que se complete
                solucion_propuesta='',
                tipo_solucion='correctiva'  # Valor por defecto
            )
            diagnostico.save()
            
            # Cambiar estado del equipo
            equipo.estado = 'en_diagnostico'
            equipo.save()
            
            messages.success(request, f'Equipo de {equipo.cliente.nombre} asignado para diagnóstico.')
            return redirect('diagnostico:asignar_diagnostico')
    
    return render(request, 'diagnostico/asignar.html', {
        'equipos_sin_diagnostico': equipos_sin_diagnostico,
        'diagnosticos_pendientes': diagnosticos_pendientes
    })

@login_required
def evaluar_diagnostico(request, id=None):
    # Si se proporciona un ID, es edición. Si no, es nuevo diagnóstico
    if id:
        diagnostico = get_object_or_404(Diagnostico, id=id, tecnico=request.user)
        equipo = diagnostico.equipo
    else:
        # Buscar un diagnóstico pendiente del usuario actual
        diagnostico = Diagnostico.objects.filter(
            tecnico=request.user,
            descripcion_diagnostico=''
        ).first()
        equipo = diagnostico.equipo if diagnostico else None
    
    if not diagnostico and not id:
        messages.warning(request, 'No tienes equipos asignados para diagnosticar.')
        return redirect('diagnostico:asignar_diagnostico')
    
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            diagnostico_obj = form.save()
            
            # Actualizar estado del equipo
            equipo = diagnostico_obj.equipo
            equipo.estado = 'reparado'
            equipo.save()
            
            messages.success(request, f'Diagnóstico para {equipo.cliente.nombre} registrado correctamente.')
            return redirect('diagnostico:listado_diagnosticos')
    else:
        form = DiagnosticoForm(instance=diagnostico)
    
    return render(request, 'diagnostico/evaluar.html', {
        'form': form,
        'diagnostico': diagnostico,
        'equipo': equipo
    })

@login_required
def listado_diagnosticos(request):
    diagnosticos_completos = Diagnostico.objects.exclude(
        descripcion_diagnostico=''
    ).order_by('-fecha_diagnostico')
    
    return render(request, 'diagnostico/listado.html', {
        'diagnosticos': diagnosticos_completos
    })

@login_required
def detalle_diagnostico(request, id):
    diagnostico = get_object_or_404(Diagnostico, id=id)
    return render(request, 'diagnostico/detalle.html', {
        'diagnostico': diagnostico
    })