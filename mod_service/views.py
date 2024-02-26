from .models import tipo_servicio, producto
from rest_framework import viewsets
from .serializer import TipoServicioSerializer, ProductoSerializer

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = tipo_servicio.objects.all()
    serializer_class = TipoServicioSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

