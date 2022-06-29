from django.db import models

# Create your models here.
class Consolas(models.Model):
    nombre = models.CharField(max_length=(20))
    modelo = models.CharField(max_length=(20))
    stock = models.IntegerField()
    def __str__(self):
        return f"Consolas: {self.nombre} - Modelo: {self.modelo}"

class Vendedores(models.Model):
    nombre = models.CharField(max_length=(20))
    apellido = models.CharField(max_length=(20))
    email = models.EmailField()

class Distribuidores(models.Model):
    empresa = models.CharField(max_length=(20))
    ingreso = models.IntegerField()

