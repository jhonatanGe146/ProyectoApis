from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'habitacion', views.HabitacionViewSet)
router.register(r'tipohab', views.TipoHabitacionViewSet)
router.register(r'estadohab', views.EstadoHabitacionViewSet)
router.register(r'inventariohab', views.InventarioXHabitacionViewSet)
urlpatterns = [
     path('', include(router.urls)),     
]

