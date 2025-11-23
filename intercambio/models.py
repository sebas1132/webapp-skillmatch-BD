# intercambio/models.py

from django.db import models
from django.utils import timezone
# Importamos los modelos necesarios de 'accounts'
from accounts.models import Usuario, Habilidad 

# --- 1. INTERCAMBIO (INTERCAMBIO) ---
class Intercambio(models.Model):
    # PK: id_intercambio (VARCHAR(10))
    id_intercambio = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # FK a Habilidad (HABILIDAD_FK)
    habilidad = models.ForeignKey(
        Habilidad, 
        on_delete=models.CASCADE,
        verbose_name='Habilidad Relacionada'
    )
    
    # Campos de Datos
    estado_creacion = models.CharField(max_length=20)
    fecha_creacion = models.DateField(default=timezone.now)
    fecha_actualizacion = models.DateField(default=timezone.now) 

    class Meta:
        verbose_name = "Intercambio de Habilidad"
        verbose_name_plural = "Intercambios de Habilidades"

    def __str__(self):
        return f"Intercambio #{self.id_intercambio} - {self.habilidad.nombre_habilidad}"


# --- 2. USUARIO INTERCAMBIO (USUARIO_INTERCAMBIO) ---
# Esta es la tabla central de la transacción, con múltiples FKs a Usuario e Intercambio.
class UsuarioIntercambio(models.Model):
    # PK: id_usuario_intercambio (VARCHAR(10))
    id_usuario_intercambio = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # 1. FK a Usuario Solicitante (Self-referential FK con related_name)
    usuario_solicitante = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='intercambios_solicitados', # Nombre para acceder desde el objeto Usuario
        verbose_name='Solicitante'
    )
    
    # 2. FK a Usuario Receptor
    usuario_receptor = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE, 
        related_name='intercambios_recibidos', # Nombre para acceder desde el objeto Usuario
        verbose_name='Receptor'
    )
    
    # 3. FK a Intercambio Principal
    intercambio = models.ForeignKey(
        Intercambio, 
        on_delete=models.CASCADE, 
        related_name='transacciones_relacionadas',
        verbose_name='Intercambio Principal'
    )
    
    # 4. FK a Intercambio Ofrecido (Referencia a lo que el solicitante ofrece)
    inter_ofrecido = models.ForeignKey(
        Intercambio, 
        on_delete=models.SET_NULL, # Si el intercambio ofrecido se elimina, se pone a NULL.
        related_name='ofrecido_en_transacciones',
        null=True, # Permite valores nulos
        blank=True, # Permite dejar el campo vacío en formularios
        verbose_name='Intercambio Ofrecido'
    )
    
    # 5. FK a Intercambio Buscado (Referencia a lo que el solicitante busca)
    inter_buscado = models.ForeignKey(
        Intercambio, 
        on_delete=models.SET_NULL,
        related_name='buscado_en_transacciones',
        null=True,
        blank=True,
        verbose_name='Intercambio Buscado'
    )
    
    # Campos adicionales del esquema original
    # Nota: Los campos id_inter_ofrecido e id_inter_buscado son las FKs que acabamos de definir.

    class Meta:
        verbose_name = "Transacción de Usuario-Intercambio"
        verbose_name_plural = "Transacciones de Usuarios"

    def __str__(self):
        return f"Transacción {self.id_usuario_intercambio}: {self.usuario_solicitante.id_usuario} -> {self.usuario_receptor.id_usuario}"


# --- 3. REPORTE (REPORTE) ---
class Reporte(models.Model):
    # PK: id_reporte (VARCHAR(10))
    id_reporte = models.CharField(
        primary_key=True, 
        max_length=10
    ) 
    
    # FK a Usuario Intercambio (USUARIO_INTERCAMBIO_FK)
    usuario_intercambio = models.ForeignKey(
        UsuarioIntercambio, 
        on_delete=models.CASCADE,
        verbose_name='Transacción Reportada'
    )

    # Campos de Datos
    motivo = models.CharField(max_length=100)
    descripcion_reporte = models.TextField(verbose_name='Descripción') # Usamos TextField para CLOB
    estado_reporte = models.CharField(max_length=20)
    justificacion_admin = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return f"Reporte #{self.id_reporte} - {self.estado_reporte}"