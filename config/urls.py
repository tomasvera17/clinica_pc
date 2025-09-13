from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('recepcion/', include('recepcion.urls')),
    path('diagnostico/', include('diagnostico.urls')),
]
