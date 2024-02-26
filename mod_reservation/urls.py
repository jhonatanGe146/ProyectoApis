from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reserva', views.ReservaViewSet)
router.register(r'huexres', views.HuespedxReservaViewSet)
router.register(r'habxres', views.HabitacionxReservaViewSet)


urlpatterns = [
    path('', include(router.urls)),
      
]

