from django import forms
from .models import Entrega

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['diagnostico', 'entregado_por', 'notas_entrega']