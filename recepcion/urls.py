from django.urls import path
from .views import registrar_equipo, listado_equipos, detalle_equipo, editar_equipo, eliminar_equipo
app_name = 'recepcion'
urlpatterns = [
    path('registrar/', registrar_equipo, name='registrar_equipo'),
    path('listado/', listado_equipos, name='listado_equipos'),
    path('detalle/<int:id>/', detalle_equipo, name='detalle_equipo'),
    path('editar/<int:id>/', editar_equipo, name='editar_equipo'),
    path('eliminar/<int:id>/', eliminar_equipo, name='eliminar_equipo'),
]