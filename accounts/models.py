# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Recomendación: Aunque tu esquema es simple, si quieres usarlo para login 
# en Django, debe heredar de AbstractBaseUser y/o PermissionsMixin.
# Por simplicidad, aquí usamos models.Model con los campos de tu esquema.

class Usuario(models.Model):
    # Clave Primaria (PK): id_usuario (VARCHAR(10))
    id_usuario = models.CharField(
        primary_key=True, 
        max_length=10,
        verbose_name='ID de Usuario' # Nombre descriptivo en la interfaz
    ) 
    
    # Datos Personales
    nombre = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    # Datos Institucionales/Login
    correo_institucional = models.EmailField(
        max_length=100, 
        unique=True, # El correo suele ser único para el login
        verbose_name='Correo Institucional'
    )
    password_hash = models.CharField(max_length=255) # Guarda la contraseña hasheada
    rol = models.CharField(max_length=20)
    estado_cuenta = models.CharField(max_length=20)
    carrera = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Usuario del Sistema"
        verbose_name_plural = "Usuarios del Sistema"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.id_usuario})"
    
# accounts/models.py (Continuación)

# HABILIDAD
class Habilidad(models.Model):
    id_habilidad = models.CharField(primary_key=True, max_length=10)
    nombre_habilidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nombre_habilidad

# INSIGNIA
class Insignia(models.Model):
    id_insignia = models.CharField(primary_key=True, max_length=10)
    nombre_insignia = models.CharField(max_length=100)
    descripcion_insignia = models.CharField(max_length=500)
    requisitos = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre_insignia