from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Articulo(models.Model):
    modelo = models.CharField(max_length=18)
    nombre = models.CharField(max_length=50)

class Variante(models.Model):
    articulo = ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
    talla = models.CharField(max_length=4)
    upc = models.CharField(max_length=15)
    ean = models.CharField(max_length=15, null=True)

class Inventario(models.Model):
    variante = ForeignKey(Variante, on_delete=models.CASCADE, null=True)
    invsistema = models.CharField(max_length=6)
    invscan = models.CharField(max_length=6)