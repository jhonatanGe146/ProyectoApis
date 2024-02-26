from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'factura', views.FacturaViewSet)
router.register(r'detallesfac', views.DetallesFacturaViewSet)
router.register(r'metodospago', views.MetodoPagoViewSet)
router.register(r'metodosfactura', views.MetodoPago_FacturaViewSet)

urlpatterns = [
     path('', include(router.urls)),
     
]

