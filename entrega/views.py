from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from diagnostico.models import Diagnostico
from recepcion.models import Equipo
from .models import Entrega
from .forms import EntregaForm

@login_required
def verificar_estado(request):
    nombre_cliente = request.GET.get('nombre_cliente', '')
    equipo_encontrado = None
    diagnostico_encontrado = None
    entrega_encontrada = None
    
    if nombre_cliente:
        # Buscar equipos por nombre de cliente
        equipos = Equipo.objects.filter(
            cliente__nombre__icontains=nombre_cliente
        )
        
        if equipos.exists():
            equipo_encontrado = equipos.first()
            # Buscar diagnóstico asociado
            diagnostico_encontrado = Diagnostico.objects.filter(
                equipo=equipo_encontrado
            ).first()
            # Buscar entrega asociada
            entrega_encontrada = Entrega.objects.filter(
                diagnostico=diagnostico_encontrado
            ).first()
    
    return render(request, 'entrega/verificar.html', {
        'equipo': equipo_encontrado,
        'diagnostico': diagnostico_encontrado,
        'entrega': entrega_encontrada,
        'nombre_buscado': nombre_cliente
    })

@login_required
def reporte_entrega(request):
    # Equipos que tienen diagnóstico completado pero no han sido entregados
    equipos_para_entrega = Equipo.objects.filter(
        estado='reparado'
    ).exclude(
        diagnostico__isnull=True
    ).exclude(
        diagnostico__entrega__isnull=False
    )
    
    if request.method == 'POST':
        diagnostico_id = request.POST.get('diagnostico')
        notas_entrega = request.POST.get('notas_entrega')
        
        if diagnostico_id:
            diagnostico = get_object_or_404(Diagnostico, id=diagnostico_id)
            
            # Crear registro de entrega
            entrega = Entrega(
                diagnostico=diagnostico,
                entregado_por=request.user,
                notas_entrega=notas_entrega
            )
            entrega.save()
            
            # Actualizar estado del equipo
            equipo = diagnostico.equipo
            equipo.estado = 'entregado'
            equipo.save()
            
            messages.success(request, f'Entrega de {equipo.cliente.nombre} registrada correctamente.')
            return redirect('entrega:verificar_estado')
    
    return render(request, 'entrega/reporte.html', {
        'equipos_para_entrega': equipos_para_entrega
    })

@login_required
def comprobante_entrega(request):
    nombre_cliente = request.GET.get('nombre_cliente', '')
    equipo_encontrado = None
    diagnostico_encontrado = None
    entrega_encontrada = None
    
    # Obtener fecha actual en zona horaria de Chile
    fecha_actual = timezone.now().strftime("%d/%m/%Y %H:%M")
    
    if nombre_cliente:
        # Buscar equipos entregados por nombre de cliente
        equipos = Equipo.objects.filter(
            cliente__nombre__icontains=nombre_cliente,
            estado='entregado'
        )
        
        if equipos.exists():
            equipo_encontrado = equipos.first()
            diagnostico_encontrado = Diagnostico.objects.filter(
                equipo=equipo_encontrado
            ).first()
            entrega_encontrada = Entrega.objects.filter(
                diagnostico=diagnostico_encontrado
            ).first()
    
    return render(request, 'entrega/comprobante.html', {
        'equipo': equipo_encontrado,
        'diagnostico': diagnostico_encontrado,
        'entrega': entrega_encontrada,
        'nombre_buscado': nombre_cliente,
        'fecha_actual': fecha_actual
    })

@login_required
def listado_entregas(request):
    entregas = Entrega.objects.all().order_by('-fecha_entrega')
    return render(request, 'entrega/listado.html', {
        'entregas': entregas
    })