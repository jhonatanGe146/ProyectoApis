from django.db import models

# Create your models here.
class tipo_servicio (models.Model):
    IDTIPOSERVICIO =  models.AutoField(primary_key=True, null=False)
    TIPO_SERVICIO = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.TIPO_SERVICIO

class producto (models.Model):
    IDPRODUCTO =  models.AutoField(primary_key=True, null=False)
    NOMBRE_PRODUCTO =  models.CharField(max_length=45)
    VALOR =  models.DecimalField(max_digits=10, decimal_places=2, null=False)
    TIPO_SERVICIO_IDTIPOSERVICIO = models.ForeignKey(
        tipo_servicio, 
        on_delete= models.CASCADE
    )
    def __str__(self):
        return self.NOMBRE_PRODUCTO
