from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Importamos solo el formulario de registro que TÚ manejas
from accounts.forms import RegistroUsuarioForm 

# ---------------------------------------------------------
# 1. VISTA DEL DASHBOARD (Versión Simulada / Mock)
# ---------------------------------------------------------
@login_required(login_url='login')
def dashboard(request):
    usuario = request.user

    # --- DATOS SIMULADOS (MOCK DATA) ---
    # Estos datos fijos nos sirven para diseñar sin errores de BD.
    # Cuando tu compañero termine, borraremos esto y descomentaremos las consultas reales.
    
    # 1. Lista de Activos (Caja Verde)
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

    # 2. Lista de Finalizados (Caja Gris)
    finalizados = [
        {
            'habilidad_buscada': 'Matemáticas I', 
            'habilidad_ofrecida': 'Historia', 
            'receptor': 'Pedro P.', 
            'estado': 'Completado', 
            'fecha': '10/11/2025'
        },
        {
            'habilidad_buscada': 'Excel', 
            'habilidad_ofrecida': 'Word', 
            'receptor': 'Maria T.', 
            'estado': 'Completado', 
            'fecha': '05/11/2025'
        },
    ]

    # 3. Lista de Cancelados (Caja Roja)
    cancelados = [
        {
            'habilidad_buscada': 'Guitarra', 
            'habilidad_ofrecida': 'Canto', 
            'receptor': 'Juan D.', 
            'estado': 'Cancelado', 
            'fecha': '01/11/2025'
        },
    ]

    # 4. Notificaciones Simuladas
    notificaciones = [
        {'mensaje': 'Tu solicitud a Ana García fue aceptada', 'tiempo': 'Hace 2 horas'},
        {'mensaje': 'Bienvenido a SkillMatch', 'tiempo': 'Ayer'},
    ]
    
    notificaciones_count = 2 # Número para la campanita roja

    # Totales para el Resumen (Estadísticas)
    # Simulamos que hay 120 usuarios y 5 intercambios activos en toda la plataforma
    total_intercambios_activos = 5
    total_usuarios = 120

    context = {
        'usuario': usuario,
        'mis_intercambios': activos, # Para el resumen de arriba
        'activos': activos,
        'finalizados': finalizados,
        'cancelados': cancelados,
        'notificaciones': notificaciones,
        'notificaciones_count': notificaciones_count,
        'total_usuarios': total_usuarios,
        'total_intercambios': total_intercambios_activos
    }

    return render(request, 'dashboard.html', context)

# ---------------------------------------------------------
# 2. VISTA DE REGISTRO
# ---------------------------------------------------------
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'registro.html', {'form': form})

# ---------------------------------------------------------
# 3. VISTA DE PERFIL (Placeholder)
# ---------------------------------------------------------
@login_required
def perfil_habilidades(request):
    # Placeholder para que no falle urls.py
    return render(request, 'dashboard.html', {})