from rest_framework import serializers
from .models import tipo_servicio, producto

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_servicio
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = "__all__"

