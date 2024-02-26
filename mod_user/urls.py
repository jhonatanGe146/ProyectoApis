from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'tipousuario', views.TipoUsuarioViewSet)
router.register(r'tipodoc', views.TipoDocumentoViewSet)
router.register(r'estadousuario', views.EstadoUsuarioViewSet) 


urlpatterns = [
    path('', include(router.urls)),     
]

