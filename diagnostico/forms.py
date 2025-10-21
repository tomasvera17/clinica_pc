from django import forms
from .models import Diagnostico

class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ['equipo', 'tecnico', 'descripcion_diagnostico', 'solucion_propuesta', 'tipo_solucion']