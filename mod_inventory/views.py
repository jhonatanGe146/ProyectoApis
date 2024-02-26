from .models import estado_producto, categoria_inventario, inventario
from rest_framework import viewsets
from .serializer import EstadoProductoSerializer, CategoriaInventarioSerializer, InventarioSerializer

class EstadoProductoViewSet(viewsets.ModelViewSet):
    queryset = estado_producto.objects.all()
    serializer_class = EstadoProductoSerializer


class CategoriaInventarioViewSet(viewsets.ModelViewSet):
    queryset = categoria_inventario.objects.all()
    serializer_class = CategoriaInventarioSerializer



class InventarioViewSet(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = InventarioSerializer