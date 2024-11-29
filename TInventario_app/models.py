from django.db import models
from TProductos_app.models import TProducto
# Create your models here.

class TInventario(models.Model):
    inventarioid = models.IntegerField(primary_key=True)
    productoid = models.ForeignKey(TProducto,on_delete=models.CASCADE)
    cantidadinicial = models.IntegerField()
    cantidadactual = models.IntegerField()
    fechaactualizacion = models.DateField()
    ubicacion = models.CharField(max_length=100)
    notas = models.TextField()

    def __str__(self):
        return f"Inventario ID: {self.inventarioid} - Producto: {self.productoid}"