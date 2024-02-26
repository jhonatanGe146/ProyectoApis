from django.db import models

# Create your models here.
class categoria_inventario(models.Model):
    IDCATEGORIA =  models.AutoField(primary_key=True ,null=False)
    NOMBRE_CATEGORIA = models.CharField(max_length=50)
    DESCRIPCION = models.TextField(max_length=200)
  
    def __str__(self):
        return self.NOMBRE_CATEGORIA

class estado_producto (models.Model):
    IDESTADOPRODUCTO=  models.AutoField(primary_key=True, null=False)
    ESTADO = models.CharField(max_length=20)



class inventario(models.Model):
    IDINVENTARIO =  models.AutoField(primary_key=True, null=False)
    NOMBRE_PRODUCTO = models.CharField(max_length=60)
    DESCRIPCION_PRODUCTO = models.TextField(max_length=300)
    ESTADO_PRODUCTO_IDESTADOPRODUCTO = models.ForeignKey(
        estado_producto,
        on_delete=models.PROTECT,
    )
    CATEGORIA_IDCATEGORIA= models.ForeignKey(
        categoria_inventario,
        on_delete=models.CASCADE,  
    )
   
    def __str__(self):
        return (f"{self.NOMBRE_PRODUCTO} --> {self.CATEGORIA_IDCATEGORIA}")
