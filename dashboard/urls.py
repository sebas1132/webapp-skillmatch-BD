from django.urls import path
from . import views

urlpatterns = [
    # Ruta: /dashboard/
    path('dashboard/', views.dashboard, name='dashboard'),

    # Rutas auxiliares (Registro y Perfil)
    # Las mantenemos aquí para que tu módulo sea funcional por sí solo mientras desarrollas
    path('registro/', views.registro, name='registro'),
    path('perfil/habilidades/', views.perfil_habilidades, name='perfil_habilidades'),
]