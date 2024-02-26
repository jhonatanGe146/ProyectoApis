from django.contrib import admin
from . models import categoria_inventario, estado_producto, inventario

# Register your models here.
admin.site.register(categoria_inventario)
admin.site.register(estado_producto)
admin.site.register(inventario)