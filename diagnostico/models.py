from django.db import models
from django.contrib.auth import get_user_model
from recepcion.models import Equipo

Usuario = get_user_model()

class Diagnostico(models.Model):
    equipo = models.OneToOneField(Equipo, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)  # Solo técnicos/admins
    descripcion_diagnostico = models.TextField()
    solucion_propuesta = models.TextField()
    tipo_solucion = models.CharField(max_length=50, choices=[('correctiva', 'Correctiva'), ('preventiva', 'Preventiva'), ('predictiva', 'Predictiva')])
    fecha_diagnostico = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnóstico de {self.equipo}"