from django.urls import path
from .views import vista_login, cerrar_sesion, registro_usuario

urlpatterns = [
    path('', vista_login, name= 'login'),
    path('logout/', cerrar_sesion, name= 'logout'),
    path('registro/', registro_usuario, name='registro_usuario'),
]
