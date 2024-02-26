from .models import huesped
from rest_framework import viewsets
from .serializer import HuespedSerializer

class HuespedViewSet(viewsets.ModelViewSet):
    queryset = huesped.objects.all()
    serializer_class = HuespedSerializer

