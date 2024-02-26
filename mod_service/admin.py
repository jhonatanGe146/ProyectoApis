from django.contrib import admin
from . models import tipo_servicio, producto

# Register your models here.
admin.site.register(tipo_servicio)
admin.site.register(producto)