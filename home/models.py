from django.db import models

# Create your models here.
class Administrador(models.Model):
    nombre = models.CharField(max_length=(20))
    apellido = models.CharField(max_length=(20))
    email = models.IntegerField()
    def __str__(self):
        return f"Administrador: {self.nombre} - Modelo: {self.apellido} - Stock: {self.email}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=(20))
    apellido = models.CharField(max_length=(20))
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Distribuidores(models.Model):
    nombre = models.CharField(max_length=(20))
    ingreso = models.IntegerField()
    def __srt__(self):
        return f"Empresa: {self.nombre} - Ingreso: {self.ingreso}"

class Caja(models.Model):
    fecha = models.DateField(auto_now_add=True, null=True)
    ingreso = models.IntegerField()
    salida = models.IntegerField()