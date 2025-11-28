from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cliente, Equipo
from .forms import ClienteForm, EquipoForm

@login_required
def registrar_equipo(request):
    if request.method == 'POST':
        # Primero manejar el formulario de cliente
        cliente_form = ClienteForm(request.POST)
        equipo_form = EquipoForm(request.POST)

        if cliente_form.is_valid() and equipo_form.is_valid():
            # Guardar el cliente
            cliente = cliente_form.save()


            equipo = equipo_form.save(commit=False)
            equipo.cliente = cliente
            equipo.recepcionista = request.user
            equipo.save()

            messages.success(request, f'Equipo de {cliente.nombre} registrado correctamente.')
            return redirect('recepcion:listado_equipos')
    else:
        cliente_form = ClienteForm()
        equipo_form = EquipoForm()

    return render(request, 'recepcion/registrar.html', {
        'cliente_form': cliente_form,
        'equipo_form': equipo_form
    })

@login_required
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=equipo.cliente)
        equipo_form = EquipoForm(request.POST, instance=equipo)
        
        if cliente_form.is_valid() and equipo_form.is_valid():
            cliente_form.save()
            equipo_form.save()
            messages.success(request, f'Equipo de {equipo.cliente.nombre} actualizado correctamente.')
            return redirect('recepcion:listado_equipos')
    else:
        cliente_form = ClienteForm(instance=equipo.cliente)
        equipo_form = EquipoForm(instance=equipo)
    
    return render(request, 'recepcion/editar.html', {
        'cliente_form': cliente_form,
        'equipo_form': equipo_form,
        'equipo': equipo
    })

@login_required
def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    nombre_cliente = equipo.cliente.nombre
    
    if request.method == 'POST':
        # Eliminar también el cliente asociado
        cliente = equipo.cliente
        equipo.delete()
        cliente.delete()
        
        messages.success(request, f'Equipo de {nombre_cliente} eliminado correctamente.')
        return redirect('recepcion:listado_equipos')
    
    return render(request, 'recepcion/eliminar.html', {'equipo': equipo})

@login_required
def listado_equipos(request):
    equipos = Equipo.objects.all().order_by('-fecha_recepcion')
    return render(request, 'recepcion/listado.html', {
        'equipos': equipos
    })

@login_required
def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'recepcion/detalle.html', {'equipo': equipo})