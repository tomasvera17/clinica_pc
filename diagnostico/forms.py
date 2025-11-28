from django import forms
from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['descripcion_diagnostico', 'solucion_propuesta', 'tipo_solucion']
        widgets = {
            'descripcion_diagnostico': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describa el problema técnico encontrado...'
            }),
            'solucion_propuesta': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Describa la solución aplicada...'
            }),
            'tipo_solucion': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'descripcion_diagnostico': 'Diagnóstico Técnico',
            'solucion_propuesta': 'Solución Aplicada',
            'tipo_solucion': 'Tipo de Solución'
        }