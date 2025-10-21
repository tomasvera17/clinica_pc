from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('tecnico', 'Técnico'),
        ('admin', 'Administrador'),
    ]
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO, default='admin')
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)
    def __str__(self):
        return f"{self.username} ({self.tipo_usuario})"
