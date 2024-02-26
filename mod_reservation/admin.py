from django.contrib import admin
from . models import estado_reserva, reserva, huesped_reserva, habitacion_reserva

# Register your models here.
admin.site.register(estado_reserva)
admin.site.register(reserva)
admin.site.register(huesped_reserva)
admin.site.register(habitacion_reserva)