from rest_framework import serializers
from .models import reserva,huesped_reserva,habitacion_reserva, estado_reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = "__all__"

class HuespedxReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = huesped_reserva
        fields = "__all__"

class HabitacionxReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitacion_reserva
        fields = "__all__"

class EstadoReservaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = estado_reserva
        fields = "__all__"