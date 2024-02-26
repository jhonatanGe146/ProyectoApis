from rest_framework import serializers
from .models import estado_producto, categoria_inventario, inventario

class EstadoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estado_producto
        fields = "__all__"

class CategoriaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria_inventario
        fields = "__all__"

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        fields = "__all__"