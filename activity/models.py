from asyncio.windows_events import NULL
from django.db import models


# Create your models here.

class Distribuidores(models.Model):
    empresa = models.CharField(max_length=40)
    def __srt__(self):
        return f"Empresa: {self.empresa}"

class Caja(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    entrada = models.IntegerField()
    salida = models.IntegerField()
    motivo = models.CharField(max_length=(214))
    total = models.IntegerField(null=True)

