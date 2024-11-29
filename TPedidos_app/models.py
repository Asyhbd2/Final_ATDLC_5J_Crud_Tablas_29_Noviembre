from django.db import models
from TClientes_app.models import TCliente
# Create your models here.

class TPedido(models.Model):
    pedidoid = models.IntegerField(primary_key=True)
    clienteid = models.ForeignKey(TCliente, on_delete=models.CASCADE)
    fechapedido = models.DateField()
    total = models.DecimalField(max_digits=7,decimal_places=2)
    estado = models.CharField(max_length=50)
    formpago = models.CharField(max_length=50)
    fechaentrega = models.DateField()

    def __str__(self):
        return f"Cliente: {self.clienteid} - Pedido: {self.pedidoid}"
    
