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
def listado_equipos(request):
    equipos = Equipo.objects.all().order_by('-fecha_recepcion')
    return render(request, 'recepcion/listado.html', {
        'equipos': equipos
    })

@login_required
def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'recepcion/detalle.html', {'equipo': equipo})