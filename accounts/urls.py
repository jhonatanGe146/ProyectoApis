from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'tipousuario', views.TipoUsuarioViewSet)
router.register(r'tipodoc', views.TipoDocumentoViewSet)
router.register(r'estadousuario', views.EstadoUsuarioViewSet) 


from accounts.views import (

    signup,
    login,
    TestView,
    logout,

)

app_name = "accounts"

urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', login, name="login"),
    path('test-view', TestView, name="test-view"),
    path('logout', logout, name="logout"),
    path('', include(router.urls)),   
      
]