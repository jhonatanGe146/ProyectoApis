from django.db import models
from django.utils import timezone

default_value = timezone.now()

class huesped(models.Model):
    NRODOCUMENTO = models.CharField(primary_key=True, null=False, max_length=10)
    NOMBRE = models.CharField(max_length=30)
    APELLIDO = models.CharField(max_length=30)
    EMAIL = models.EmailField(unique=True)
    TELEFONO = models.CharField(max_length=12)

    def __str__(self):
        return (f'{self.NRODOCUMENTO} || {self.NOMBRE} || {self.APELLIDO}  ')
