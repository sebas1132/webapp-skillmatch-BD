from django.contrib import admin
from django.urls import path, include
# from django.shortcuts import redirect (Ya no es estrictamente necesario si usamos include, pero puedes dejarlo)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. App de tus compañeros (Maneja Login, Home, etc.)
    path('', include('accounts.urls')), 
    
    # 2. TU App (Maneja Dashboard, y tus vistas temporales de Registro/Perfil)
    # Al ponerlo también en '', las rutas se suman.
    # Django buscará: localhost:8000/dashboard/ -> Irá a dashboard.urls
    path('', include('dashboard.urls')), 
]