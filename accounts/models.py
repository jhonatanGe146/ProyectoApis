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
    
class tipo_persona (models.Model):
    IDTIPOPERSONA =  models.AutoField(primary_key=True, null=False)
    TIPO_PERSONA = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.TIPO_PERSONA


class tipo_documento (models.Model):
    IDTIPODOCUMENTO = models.AutoField(primary_key=True, null=False)
    TIPO_DOCUMENTO = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.TIPO_DOCUMENTO

class estado_usuario (models.Model):
    IDESTADO =  models.AutoField(primary_key=True, null=False)
    ESTADO = models.CharField(max_length=10)

    def __str__(self):
        return self.ESTADO

class persona(AbstractUser):
    TIPO_DOCUMENTO_IDTIPODOCUMENTO = models.ForeignKey(tipo_documento,
                                                       on_delete=models.PROTECT,
                                                       null=True, blank=True)
    NRODOCUMENTO = models.CharField(max_length=10, primary_key=True)
    NOMBRE = models.CharField(max_length=70)
    APELLIDO = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=45)
    TELEFONO = models.CharField(max_length=15)
    TIPO_PERSONA_IDTIPOPERSONA = models.ForeignKey(tipo_persona,
                                                    on_delete=models.PROTECT,
                                                    null=True, blank=True)
    ESTADO_USUARIO_IDESTADO = models.ForeignKey(estado_usuario,
                                                on_delete=models.PROTECT,
                                                null=True, blank=True)

    def __str__(self):
        return (f'{self.NRODOCUMENTO}  {self.NOMBRE} --> {self.APELLIDO}')

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def created_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)