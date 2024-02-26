from django.db import models
from django.utils import timezone

default_value = timezone.now()

class huesped(models.Model):
    IDHUESPED =  models.AutoField(primary_key=True, null=False)
    NRODOCUMENTO = models.CharField(max_length=10)
    NOMBRE = models.CharField(max_length=70)
    APELLIDO = models.CharField(max_length=70)
    EMAIL = models.EmailField(unique=True)
    TELEFONO = models.CharField(max_length=15)

    def __str__(self):
        return (f'{self.NRODOCUMENTO} || {self.NOMBRE} || {self.APELLIDO}  ')