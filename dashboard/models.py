# dashboard/models.py

from django.db import models
from django.utils import timezone
from accounts.models import Usuario # Importamos Usuario

# --- NOTIFICACION (NOTIFICACION) ---
class Notificacion(models.Model):
    # PK: id_notificacion (VARCHAR(10))
    id_notificacion = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # FK a Usuario (USUARIO_FK)
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        verbose_name='Usuario Destino'
    ) 

    # Campos de Datos
    mensaje = models.CharField(max_length=1000)
    estado_notificacion = models.CharField(max_length=20)
    fecha_creacion = models.DateField(default=timezone.now)
    tipo_notificacion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Notificación"
        verbose_name_plural = "Notificaciones"

    def __str__(self):
        return f"Notif. {self.id_notificacion} para {self.usuario.id_usuario}"