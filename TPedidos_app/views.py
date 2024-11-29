from django.shortcuts import render, redirect
from .models import TPedido
from TClientes_app.models import TCliente  # Importamos el modelo del cliente
# Create your views here.

def inicio_vistaPedidos(request):
    lospedidos = TPedido.objects.all()
    return render(request, "gestionarPedido.html", {"mispedidos": lospedidos})

def seleccionarPedido(request, pedidoid):
    pedido = TPedido.objects.get(pedidoid=pedidoid)
    return render(request, "editarPedido.html", {"lospedidos": pedido})

def registrarPedido(request):
    pedidoid = request.POST["numid"]
    clienteid = TCliente.objects.get(clienteid=request.POST["clienteid"])  # Obtenemos el cliente asociado
    fechapedido = request.POST["datepedido"]
    total = request.POST["decimaltotal"]
    estado = request.POST["txtestado"]
    formpago = request.POST["txtformpago"]
    fechaentrega = request.POST["dateentrega"]

    guardarPedido = TPedido.objects.create(
        pedidoid=pedidoid,
        clienteid=clienteid,
        fechapedido=fechapedido,
        total=total,
        estado=estado,
        formpago=formpago,
        fechaentrega=fechaentrega,
    )
    return redirect("inicio_vistaPedidos")

def editarPedido(request):
    pedidoid = request.POST["numid"]
    clienteid = TCliente.objects.get(clienteid=request.POST["clienteid"])  # Obtenemos el cliente asociado
    fechapedido = request.POST["datepedido"]
    total = request.POST["decimaltotal"]
    estado = request.POST["txtestado"]
    formpago = request.POST["txtformpago"]
    fechaentrega = request.POST["dateentrega"]

    pedido = TPedido.objects.get(pedidoid=pedidoid)
    pedido.clienteid = clienteid
    pedido.fechapedido = fechapedido
    pedido.total = total
    pedido.estado = estado
    pedido.formpago = formpago
    pedido.fechaentrega = fechaentrega

    pedido.save()
    return redirect("inicio_vistaPedidos")

def borrarPedido(request, pedidoid):
    pedido = TPedido.objects.get(pedidoid=pedidoid)
    pedido.delete()
    return redirect("inicio_vistaPedidos")