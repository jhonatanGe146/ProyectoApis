from django.contrib import admin
from . models import estado_habitacion, tipo_habitacion, habitacion, inventario_habitacion
# Register your models here.
admin.site.register(estado_habitacion)
admin.site.register(tipo_habitacion)
admin.site.register(habitacion)
admin.site.register(inventario_habitacion)
