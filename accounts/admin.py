from django.contrib import admin
from . models import tipo_documento, tipo_persona, persona, estado_usuario
# Register your models here.
admin.site.register(tipo_persona)
admin.site.register(tipo_documento)
admin.site.register(persona)
admin.site.register(estado_usuario)


# Register your models here.
