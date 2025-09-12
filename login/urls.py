from django.urls import path
from .views import vista_login, cerrar_sesion

urlpatterns = [
    path('', vista_login, name= 'login'),
    path('logout/', cerrar_sesion, name= 'logout'),
]
