from django.urls import path
from .views import asignar_diagnostico, evaluar_diagnostico, listado_diagnosticos, detalle_diagnostico

app_name = 'diagnostico'

urlpatterns = [
    path('asignar/', asignar_diagnostico, name='asignar_diagnostico'),
    path('evaluar/', evaluar_diagnostico, name='evaluar_diagnostico'),  
    path('evaluar/<int:id>/', evaluar_diagnostico, name='editar_diagnostico'),  
    path('listado/', listado_diagnosticos, name='listado_diagnosticos'),
    path('detalle/<int:id>/', detalle_diagnostico, name='detalle_diagnostico'),
]