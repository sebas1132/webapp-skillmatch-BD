from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordResetForm


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # INTENTO DE AUTENTICACIÓN
            print(f"Intentando loguear a: {email}") 
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                print("¡Usuario encontrado! Redirigiendo...")
                login(request, user)
                return redirect('dashboard')  # <--- Aquí es donde queremos llegar
            else:
                print("Error: Usuario o contraseña incorrectos (authenticate devolvió None)")
                messages.error(request, 'Correo o contraseña incorrectos.')
        else:
            print("Error: El formulario no es válido")
            print(form.errors) # Esto te dirá qué campo está fallando
            messages.error(request, 'Datos inválidos.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido a SkillMatch.')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


# -----------------------------------------
# 🔴 RECUPERAR CONTRASEÑA — FUNCIONAL
# -----------------------------------------

def password_reset_view(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')

            # Verificar si existe el usuario
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Este correo no está registrado.')
                return redirect('accounts:password_reset')

            # Generar nueva contraseña
            new_password = get_random_string(length=10)

            # Asignar nueva contraseña
            user.set_password(new_password)
            user.save()

            # Crear correo
            mensaje = EmailMessage(
                subject='Recuperación de contraseña - SkillMatch',
                body=f'''
Hola,

Tu nueva contraseña es: {new_password}

Por seguridad, cámbiala cuando inicies sesión.

Saludos,
SkillMatch
                ''',
                from_email=None,
                to=[email],
                cc=['noreplyskillmatch@gmail.com'],
            )

            # 🔥 VALIDAR SI SE ENVÍA EL CORREO
            try:
                enviado = mensaje.send()
            except Exception as e:
                print("ERROR SMTP:", e)
                messages.error(request, 'No se pudo enviar el correo: ' + str(e))
                return redirect('accounts:password_reset')

            if enviado == 1:
                messages.success(request, 'Hemos enviado una nueva contraseña a tu correo.')
                return redirect('accounts:login')
            else:
                messages.error(request, 'No se pudo enviar el correo. Intenta nuevamente.')
                return redirect('accounts:password_reset')

        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')

    else:
        form = CustomPasswordResetForm()
    
    return render(request, 'accounts/password_reset.html', {'form': form})


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    return render(request, 'accounts/dashboard.html')


def home_view(request):
    """Página principal pública"""
    return render(request, 'accounts/home.html')
