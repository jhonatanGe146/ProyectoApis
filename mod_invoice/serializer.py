from rest_framework import serializers
from .models import metodo_pago, metodopago_factura, factura, detalles_factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = factura
        fields = "__all__"

class DetallesFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalles_factura
        fields = "__all__"

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = metodo_pago
        fields = "__all__"

class MetodoPago_FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = metodopago_factura
        fields = "__all__"

