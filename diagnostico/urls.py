from django.urls import path
from .views import asignar_diagnostico, evaluar_diagnostico, listado_diagnosticos

urlpatterns = [
    path('asignar/', asignar_diagnostico, name='asignar_diagnostico'),
    path('evaluar/', evaluar_diagnostico, name='evaluar_diagnostico'),
    path('listado/', listado_diagnosticos, name='listado_diagnosticos'),
]