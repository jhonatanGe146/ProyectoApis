from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email = email,
            **extra_fields
        )

        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser tiene que tener is_staff en verdadero")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser tiene que tener is_superuser en verdadero")

        return self.create_user(email = email, password = password, **extra_fields)

class TipoPersona(models.Model):
    tipo_persona = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_persona

class TipoDocumento(models.Model):
    tipo_documento = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo_documento

class Persona(AbstractUser):
    id_tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, null = True)
    numero_documento = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=70, null = True)
    apellido = models.CharField(max_length=70, null = True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    telefono = models.CharField(max_length=15, null = True)
    id_tipoPersona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE, null = True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def created_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)