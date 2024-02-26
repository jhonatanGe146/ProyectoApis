from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tiposervicio', views.TipoServicioViewSet)
router.register(r'producto', views.ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
      
]

