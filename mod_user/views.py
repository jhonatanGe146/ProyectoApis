from .models import tipo_documento, tipo_persona, persona, estado_usuario
from rest_framework import viewsets
from .serializer import UsuarioSerializer, TipoDocumentoSerializer, TipoUsuarioSerializer, EstadoUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = persona.objects.all()
    serializer_class = UsuarioSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = tipo_documento.objects.all()
    serializer_class = TipoDocumentoSerializer

class EstadoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = estado_usuario.objects.all()
    serializer_class = EstadoUsuarioSerializer


class TipoUsuarioViewSet(viewsets.ModelViewSet):
    queryset = tipo_persona.objects.all()
    serializer_class = TipoUsuarioSerializer
