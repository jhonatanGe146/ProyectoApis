from django.contrib import admin
from . models import factura, metodo_pago, metodopago_factura,detalles_factura

# Register your models here.
admin.site.register(factura)
admin.site.register(metodo_pago)
admin.site.register(metodopago_factura)
admin.site.register(detalles_factura)