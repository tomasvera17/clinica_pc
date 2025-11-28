from django.urls import path
from .views import vista_login, cerrar_sesion, registro_usuario, dashboard

app_name = 'login'

urlpatterns = [
    path('', vista_login, name= 'vista_login'),
    path('logout/', cerrar_sesion, name= 'cerrar_sesion'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('dashboard/', dashboard, name='dashboard'),
]
