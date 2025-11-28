from django import forms
from .models import Cliente, Equipo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del cliente'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 1234 5678'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Dirección del cliente'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['tipo_equipo', 'marca', 'modelo', 'descripcion_problema', 'estado']
        widgets = {
            'tipo_equipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Laptop, Desktop, Tablet, etc.'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca del equipo'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo del equipo'}),
            'descripcion_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describa el problema reportado por el cliente'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'descripcion_problema': 'Problema Reportado',
        }