from django.db import models

# Create your models here.
class tipo_persona (models.Model):
    IDTIPOPERSONA =  models.AutoField(primary_key=True, null=False)
    TIPO_PERSONA = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.TIPO_PERSONA

class tipo_documento (models.Model):
    IDTIPODOCUMENTO = models.AutoField(primary_key=True, null=False)
    TIPO_DOCUMENTO = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.TIPO_DOCUMENTO
    
class estado_usuario (models.Model):
    IDESTADO =  models.AutoField(primary_key=True, null=False)
    ESTADO = models.CharField(max_length=10)

    def __str__(self):
        return self.ESTADO

class persona(models.Model):
    TIPO_DOCUMENTO_IDTIPODOCUMENTO = models.ForeignKey(tipo_documento,
     on_delete=models.PROTECT,
    )
    NRODOCUMENTO = models.CharField(max_length=10, primary_key=True)
    NOMBRE = models.CharField(max_length=70)
    APELLIDO = models.CharField(max_length=70)
    EMAIL = models.EmailField(max_length=100, unique=True)
    TELEFONO = models.CharField(max_length=15)
    TIPO_PERSONA_IDTIPOPERSONA = models.ForeignKey(tipo_persona,
    on_delete=models.PROTECT,)
    CONTRASENA = models.CharField(max_length=95)
    ESTADO_USUARIO_IDESTADO = models.ForeignKey(estado_usuario,
    on_delete=models.PROTECT)

    def __str__(self):
        return (f'{self.NRODOCUMENTO}  {self.NOMBRE} --> {self.APELLIDO}')
    