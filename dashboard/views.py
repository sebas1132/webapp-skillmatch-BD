from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from .models import Intercambio, Notificacion
# Asegúrate de que en forms.py exista RegistroUsuarioForm
from .forms import RegistroUsuarioForm 

# ---------------------------------------------------------
# 1. VISTA DEL DASHBOARD (Nuevo Diseño)
# ---------------------------------------------------------
@login_required(login_url='login')
def dashboard(request):
    usuario = request.user

    # A. Mis Intercambios Activos (En Progreso o Pendiente)
    mis_intercambios = Intercambio.objects.filter(
        (Q(solicitante=usuario) | Q(receptor=usuario)) & 
        Q(estado__in=['EnProgreso', 'Pendiente'])
    ).order_by('-fecha_creacion')[:3]

    # B. Listas para las Cajas de la derecha
    # 1. Activos (para la caja verde)
    activos = Intercambio.objects.filter(
        (Q(solicitante=usuario) | Q(receptor=usuario)) & 
        Q(estado__in=['EnProgreso', 'Pendiente'])
    ).order_by('-fecha_creacion')

    # 2. Finalizados (para la caja gris)
    finalizados = Intercambio.objects.filter(
        (Q(solicitante=usuario) | Q(receptor=usuario)) & 
        Q(estado='Completado')
    ).order_by('-fecha_actualizacion')[:3]

    # 3. Cancelados (para la caja roja)
    cancelados = Intercambio.objects.filter(
        (Q(solicitante=usuario) | Q(receptor=usuario)) & 
        Q(estado__in=['Cancelado', 'Rechazado'])
    ).order_by('-fecha_actualizacion')[:3]

    # C. Notificaciones
    notificaciones = Notificacion.objects.filter(
        usuario=usuario
    ).order_by('-fecha_creacion')[:3]
    
    notificaciones_count = Notificacion.objects.filter(usuario=usuario, leida=False).count()

    context = {
        'usuario': usuario,
        'mis_intercambios': mis_intercambios, # Para el resumen
        'activos': activos,                   # Para la caja grande
        'finalizados': finalizados,
        'cancelados': cancelados,
        'notificaciones': notificaciones,
        'notificaciones_count': notificaciones_count,
    }

    return render(request, 'dashboard.html', context)

# ---------------------------------------------------------
# 2. VISTA DE REGISTRO (Restaurada)
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
# 3. VISTA DE PERFIL (Placeholder para evitar errores)
# ---------------------------------------------------------
@login_required
def perfil_habilidades(request):
    # Por ahora, redirigimos al dashboard hasta que reconstruyamos esta parte
    # o renderizamos un template "en construcción"
    return render(request, 'dashboard.html', {})