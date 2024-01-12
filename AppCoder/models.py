from django.db import models

# Create your models here.

class BebidasConAlcohol(models.Model):

    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class BebidasSinAlcohol(models.Model):

    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class Comidas(models.Model):

    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class Accesorios(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.IntegerField()
    cantidad = models.IntegerField()