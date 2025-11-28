from django import forms
from .models import Entrega
from diagnostico.models import Diagnostico

class EntregaForm(forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['diagnostico', 'notas_entrega']
        widgets = {
            'diagnostico': forms.Select(attrs={
                'class': 'form-select'
            }),
            'notas_entrega': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Observaciones adicionales sobre la entrega...'
            }),
        }
        labels = {
            'diagnostico': 'Seleccionar Diagnóstico',
            'notas_entrega': 'Observaciones de Entrega'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo diagnósticos que no tienen entrega
        self.fields['diagnostico'].queryset = Diagnostico.objects.filter(
            entrega__isnull=True
        ).exclude(
            descripcion_diagnostico=''
        )