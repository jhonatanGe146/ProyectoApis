from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estadoproducto', views.EstadoProductoViewSet)
router.register(r'categoria', views.CategoriaInventarioViewSet)
router.register(r'inventario', views.InventarioViewSet)



urlpatterns = [
    path('', include(router.urls)),
      
]

