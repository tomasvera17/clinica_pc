from django import forms
from .models import Cliente, Equipo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['cliente', 'descripcion_problema', 'tipo_equipo', 'marca', 'modelo', 'estado']