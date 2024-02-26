from django.contrib import admin
from .models import Persona, TipoDocumento, TipoPersona


admin.site.register(Persona)
admin.site.register(TipoDocumento)
admin.site.register(TipoPersona)