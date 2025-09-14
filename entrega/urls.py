from django.urls import path
from .views import verificar_estado, reporte_entrega, comprobante_entrega

urlpatterns = [
    path('verificar/', verificar_estado, name='verificar_estado'),
    path('reporte/', reporte_entrega, name='reporte_entrega'),
    path('comprobante/', comprobante_entrega, name='comprobante_entrega'),
]