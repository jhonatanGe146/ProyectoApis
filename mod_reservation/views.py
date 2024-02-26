from .models import reserva,huesped_reserva,habitacion_reserva, estado_reserva
from rest_framework import viewsets
from .serializer import ReservaSerializer,HuespedxReservaSerializer, HabitacionxReservaSerializer, EstadoReservaSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = ReservaSerializer


class HuespedxReservaViewSet(viewsets.ModelViewSet):
    queryset = huesped_reserva.objects.all()
    serializer_class = HuespedxReservaSerializer

class HabitacionxReservaViewSet(viewsets.ModelViewSet):
    queryset = habitacion_reserva.objects.all()
    serializer_class = HabitacionxReservaSerializer


class EstadoReservaViewSet(viewsets.ModelViewSet):
    queryset = estado_reserva.objects.all()
    serializer_class = EstadoReservaSerializer