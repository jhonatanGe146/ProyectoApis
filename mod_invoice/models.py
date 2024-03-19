from django.db import models
from mod_reservation.models import reserva
from mod_service.models import producto



class metodo_pago(models.Model):
    IDMETODOPAGO = models.AutoField(primary_key=True, null=False)
    METODO = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.METODO
    
class factura(models.Model):
    IDFACTURA = models.AutoField(primary_key=True, null=False)
    FECHA_FACTURA = models.DateField(null=False)
    MONTO_TOTAL_RESERVA = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    IDRESERVA = models.ForeignKey(reserva,
    on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.IDFACTURA} || {self.FECHA_FACTURA} || {self.MONTO_TOTAL_RESERVA}')


class metodopago_factura(models.Model):
    ID_METODO_FACTURA = models.AutoField(primary_key=True,null=False)
    FACTURA_IDFACTURA = models.ForeignKey(
        factura, 
        on_delete=models.CASCADE,
        )
    METODO_PAGO_IDMETODOPAGO = models.ForeignKey(
        metodo_pago, 
        on_delete=models.CASCADE,
    )

class detalles_factura(models.Model):
    IDDETALLESFACTURA = models.AutoField(primary_key=True, null=False)
    FACTURA_IDFACTURA = models.ForeignKey(
        factura, 
        on_delete=models.CASCADE,
        )
    CANTIDAD = models.IntegerField(null= False)
    
    PRODUCTO_IDPRODUCTO = models.ForeignKey(
        producto, 
        on_delete=models.PROTECT,
    )
    def __str__(self):
        return str(f'{self.FACTURA_IDFACTURA} || {self.CANTIDAD} ||  {self.PRODUCTO_IDPRODUCTO.NOMBRE_PRODUCTO}')

