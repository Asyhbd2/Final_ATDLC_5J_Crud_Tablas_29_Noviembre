from django.db import models

# Create your models here.

class TCliente(models.Model):
    clienteid=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=255)
    fecharegistro=models.DateField(null=False,blank=False)

    def __str__(self):
        return self.nombre