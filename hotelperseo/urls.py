"""
URL configuration for hotelperseo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import  static
from  django.conf import settings
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('usuarios/', include('accounts.urls')),
    path ('guest/', include('mod_guest.urls')),
    path ('inventory/', include('mod_inventory.urls')),
    path ('invoice/', include('mod_invoice.urls')),
    path ('reservation/', include('mod_reservation.urls')),
    path ('room/', include('mod_room.urls')),
    path ('service/', include('mod_service.urls')),
    path('', include_docs_urls(title='Api Documentation'))
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
