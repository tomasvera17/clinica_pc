from django.db import models
from django.contrib.auth import get_user_model
from diagnostico.models import Diagnostico

Usuario = get_user_model()

class Entrega(models.Model):
    diagnostico = models.OneToOneField(Diagnostico, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    entregado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # Solo técnicos/admins
    notas_entrega = models.TextField(blank=True)
    
    def __str__(self):
        return f"Entrega de {self.diagnostico.equipo}"