from django.urls import path
from . import views

urlpatterns = [
    # Solo las rutas exclusivas de tu módulo
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/habilidades/', views.perfil_habilidades, name='perfil_habilidades'),
]