from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Para el logout si accounts no lo tiene

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. App de ACCOUNTS (Maneja '', 'login/', 'register/')
    # Como tiene path('', ...), esta app controlará la página de inicio.
    path('', include('accounts.urls')), 
    
    # 2. App de DASHBOARD (Maneja 'dashboard/')
    path('', include('dashboard.urls')),
    
    # 3. Logout (Por seguridad, lo agregamos aquí si accounts no lo tiene)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]