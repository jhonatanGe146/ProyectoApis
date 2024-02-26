from .models import metodo_pago, metodopago_factura, factura, detalles_factura
from rest_framework import viewsets
from .serializer import FacturaSerializer,DetallesFacturaSerializer,MetodoPagoSerializer, MetodoPago_FacturaSerializer

# Create your views here.
class FacturaViewSet(viewsets.ModelViewSet):
    queryset = factura.objects.all()
    serializer_class = FacturaSerializer


class DetallesFacturaViewSet(viewsets.ModelViewSet):
    queryset = detalles_factura.objects.all()
    serializer_class = DetallesFacturaSerializer

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = metodo_pago.objects.all()
    serializer_class = MetodoPagoSerializer

class MetodoPago_FacturaViewSet(viewsets.ModelViewSet):
    queryset = metodopago_factura.objects.all()
    serializer_class = MetodoPago_FacturaSerializer
