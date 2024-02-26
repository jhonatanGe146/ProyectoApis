from django.db import models
from mod_inventory.models import inventario

# Create your models here.
class estado_habitacion(models.Model):
    IDESTADOHABITACION =  models.AutoField(primary_key=True, null=False)
    TIPO_ESTADO = models.CharField(max_length=20)
    DESCRIPCION = models.TextField(max_length=200)
 
    def __str__(self):
        return self.TIPO_ESTADO

 

class tipo_habitacion(models.Model):
    IDTIPOHABITACION = models.AutoField(primary_key=True, null=False) 
    TIPO_HABITACION = models.CharField(max_length=30)
    DESCRIPCION = models.TextField(max_length=200)
    PRECIOXNOCHE = models.FloatField()
    CANTIDAD_ADULTOS = models.IntegerField()
    CANTIDAD_NINOS = models.IntegerField()
    FOTO = models.ImageField(upload_to='fotos_tipoHab')

    def __str__(self):
        return self.TIPO_HABITACION


class habitacion(models.Model):
    NROHABITACION = models.CharField(max_length=4, primary_key=True, null=False)
    ESTADO_HABITACION_IDESTADOHABITACION = models.ForeignKey(
        estado_habitacion,
        on_delete=models.PROTECT,
    )
    TIPO_HABITACION_IDTIPOHABITACION = models.ForeignKey(
        tipo_habitacion,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.NROHABITACION

class inventario_habitacion (models.Model):
    ID_INVENTARIO_HABITACION =  models.AutoField(primary_key=True, null=False)
    
    INVENTARIO_IDINVENTARIO = models.ForeignKey(
        inventario, 
        on_delete=models.CASCADE,
    )
    HABITACION_NROHABITACION = models.ForeignKey(
        habitacion, 
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return (f'{self.HABITACION_NROHABITACION} --> {self.INVENTARIO_IDINVENTARIO}')