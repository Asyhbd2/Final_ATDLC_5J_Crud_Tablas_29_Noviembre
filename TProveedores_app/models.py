from django.db import models

# Create your models here.

class TProveedor(models.Model):
    proveedorid = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    fecharegistro = models.DateField()
    productosuministro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "TProveedores"