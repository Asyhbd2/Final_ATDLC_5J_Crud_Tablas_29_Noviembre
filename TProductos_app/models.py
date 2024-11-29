from django.db import models

# Create your models here.

class TProducto(models.Model):
    productoid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.IntegerField()
    fechaingreso = models.DateField()

    def __str__(self):
        return self.nombre