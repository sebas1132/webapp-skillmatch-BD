from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# CORRECCIÓN: Usamos el nombre real que tienes en accounts/forms.py
from accounts.forms import CustomUserCreationForm 

# ---------------------------------------------------------
# 1. VISTA DEL DASHBOARD (Datos Simulados / Mock)
# ---------------------------------------------------------
@login_required(login_url='login') # Asegúrate de que tu URL de login se llame 'login'
def dashboard(request):
    usuario = request.user

    # --- DATOS SIMULADOS (MOCK DATA) ---
    # Usamos esto mientras tu compañero termina la app 'intercambio'.
    
    # 1. En Progreso (Caja Verde)
    activos = [
        {
            'habilidad_buscada': 'Python Avanzado', 
            'habilidad_ofrecida': 'Inglés C1', 
            'receptor': 'Ana García', 
            'estado': 'EnProgreso', 
            'fecha': '22/11/2025'
        },
        {
            'habilidad_buscada': 'Diseño UX', 
            'habilidad_ofrecida': 'HTML5', 
            'receptor': 'Carlos López', 
            'estado': 'Pendiente', 
            'fecha': '23/11/2025'
        },
    ]

    # 2. Finalizados (Caja Gris)
    finalizados = [
        {
            'habilidad_buscada': 'Matemáticas I', 
            'habilidad_ofrecida': 'Historia', 
            'receptor': 'Pedro P.', 
            'estado': 'Completado', 
            'fecha': '10/11/2025'
        },
    ]

    # 3. Cancelados (Caja Roja)
    cancelados = [
        {
            'habilidad_buscada': 'Guitarra', 
            'habilidad_ofrecida': 'Canto', 
            'receptor': 'Juan D.', 
            'estado': 'Cancelado', 
            'fecha': '01/11/2025'
        },
    ]

    # 4. Notificaciones
    notificaciones = [
        {'mensaje': 'Tu solicitud a Ana García fue aceptada', 'tiempo': 'Hace 2 horas'},
        {'mensaje': 'Bienvenido a SkillMatch', 'tiempo': 'Ayer'},
    ]
    notificaciones_count = 2

    # Estadísticas Globales
    total_usuarios = 120
    total_intercambios = 15

    context = {
        'usuario': usuario,
        'activos': activos,
        'finalizados': finalizados,
        'cancelados': cancelados,
        'notificaciones': notificaciones,
        'notificaciones_count': notificaciones_count,
        'total_usuarios': total_usuarios,
        'total_intercambios': total_intercambios,
        'mis_intercambios': activos, # Para el resumen
    }

    return render(request, 'dashboard.html', context)


# ---------------------------------------------------------
# 3. VISTA DE PERFIL (Placeholder)
# ---------------------------------------------------------
@login_required
def perfil_habilidades(request):
    # Renderiza el dashboard temporalmente para no dar error 404
    return render(request, 'dashboard.html', {'usuario': request.user})