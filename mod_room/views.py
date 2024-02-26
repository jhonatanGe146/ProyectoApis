from .models import habitacion,estado_habitacion,tipo_habitacion, inventario_habitacion
from rest_framework import viewsets
from .serializer import HabitacionSerializer, EstadoHabitacionSerializer, TipoHabitacionSerializer,InventarioXHabitacionSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = habitacion.objects.all()
    serializer_class = HabitacionSerializer


class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = tipo_habitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

class EstadoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = estado_habitacion.objects.all()
    serializer_class = EstadoHabitacionSerializer


class InventarioXHabitacionViewSet(viewsets.ModelViewSet):
    queryset = inventario_habitacion.objects.all()
    serializer_class = InventarioXHabitacionSerializer

