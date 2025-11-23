# perfil/models.py

from django.db import models
from accounts.models import Usuario, Insignia # Importamos los modelos base

# --- 1. DISPONIBILIDAD (DISPONIBILIDAD) ---
class Disponibilidad(models.Model):
    # PK: id_disponibilidad (VARCHAR(10))
    id_disponibilidad = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # FK a Usuario (USUARIO_FK)
    # on_delete=models.CASCADE: Si se elimina el usuario, se elimina su disponibilidad.
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        verbose_name='Usuario'
    )
    
    # Campos de Disponibilidad
    dia_semana = models.CharField(max_length=10)
    hora_inicio = models.CharField(max_length=5) # Usamos CharField para mantener el formato original (ej. '09:00')
    hora_fin = models.CharField(max_length=5)
    ubicacion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Disponibilidad del Usuario"
        verbose_name_plural = "Disponibilidades"

    def __str__(self):
        return f"{self.usuario.id_usuario} disponible el {self.dia_semana}"

# --- 2. USUARIO INSIGNIA (USUARIO_INSIGNIA) ---
class UsuarioInsignia(models.Model):
    # PK: id_usuario_insignia (VARCHAR(10))
    id_usuario_insignia = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # FK a Usuario (Relation_2_USUARIO_FK)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE
    ) 
    
    # FK a Insignia (Relation_2_INSIGNIA_FK)
    insignia = models.ForeignKey(
        Insignia, 
        on_delete=models.CASCADE
    )
    
    # Campo de Datos
    fecha_obtencion = models.DateField() # Fecha de la obtención

    class Meta:
        # Define una restricción de unicidad: un usuario solo puede tener una instancia de una insignia.
        unique_together = ('usuario', 'insignia') 
        verbose_name = "Insignia Obtenida"
        verbose_name_plural = "Insignias de Usuarios"

    def __str__(self):
        return f"{self.usuario.id_usuario} - {self.insignia.nombre_insignia}"