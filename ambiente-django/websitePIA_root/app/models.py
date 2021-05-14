from django.db import models

# Create your models here.
class Estanteria(models.Model):
    descripcion = models.CharField(max_length=60)
    alto = models.FloatField()
    ancho = models.FloatField()
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Lockers(models.Model):
    descripcion = models.CharField(max_length=60)
    color = models.CharField(max_length=40)
    presentacion =models.CharField(max_length=30)
    largo = models.FloatField()
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Muebles(models.Model):
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Cajas(models.Model):
    descripcion = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
    presentacion = models.CharField(max_length=40)
    capacidad = models.FloatField()
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion