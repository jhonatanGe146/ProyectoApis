from rest_framework import serializers
from .models import habitacion, estado_habitacion, tipo_habitacion, inventario_habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitacion
        fields = "__all__"

class EstadoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = estado_habitacion
        fields = "__all__"

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_habitacion
        fields = "__all__"



class InventarioXHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario_habitacion
        fields = "__all__"