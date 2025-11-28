from django.urls import path
from .views import verificar_estado, reporte_entrega, comprobante_entrega, listado_entregas

app_name = 'entrega'

urlpatterns = [
    path('verificar/', verificar_estado, name='verificar_estado'),
    path('reporte/', reporte_entrega, name='reporte_entrega'),
    path('comprobante/', comprobante_entrega, name='comprobante_entrega'),
    path('listado/', listado_entregas, name='listado_entregas'),
]