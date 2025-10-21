from django.db import models
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    ESTADOS = [
        ('recibido', 'Recibido'),
        ('en_diagnostico', 'En Diagnóstico'),
        ('reparado', 'Reparado'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion_problema = models.TextField()
    tipo_equipo = models.CharField(max_length=50)  # e.g., 'Laptop', 'PC'
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='recibido')
    recepcionista = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  # Solo técnicos/admins

    def __str__(self):
        return f"{self.tipo_equipo} - {self.cliente.nombre}"