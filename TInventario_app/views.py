from django.shortcuts import render, redirect
from .models import TInventario
from TProductos_app.models import TProducto  # Importamos el modelo del producto
# Create your views here.

def inicio_vistaInventarios(request):
    losinventarios = TInventario.objects.all()
    return render(request, "gestionarInventario.html", {"misinventarios": losinventarios})

def seleccionarInventario(request, inventarioid):
    inventario = TInventario.objects.get(inventarioid=inventarioid)
    return render(request, "editarInventario.html", {"losinventarios": inventario})

def registrarInventario(request):
    inventarioid = request.POST["numid"]
    productoid = TProducto.objects.get(productoid=request.POST["productoid"])  # Obtenemos el producto asociado
    cantidadinicial = request.POST["cantidadinicial"]
    cantidadactual = request.POST["cantidadactual"]
    fechaactualizacion = request.POST["fechaactualizacion"]
    ubicacion = request.POST["ubicacion"]
    notas = request.POST["notas"]

    guardarInventario = TInventario.objects.create(
        inventarioid=inventarioid,
        productoid=productoid,
        cantidadinicial=cantidadinicial,
        cantidadactual=cantidadactual,
        fechaactualizacion=fechaactualizacion,
        ubicacion=ubicacion,
        notas=notas,
    )
    return redirect("inicio_vistaInventarios")

def editarInventario(request):
    inventarioid = request.POST["numid"]
    productoid = TProducto.objects.get(productoid=request.POST["productoid"])  # Obtenemos el producto asociado
    cantidadinicial = request.POST["cantidadinicial"]
    cantidadactual = request.POST["cantidadactual"]
    fechaactualizacion = request.POST["fechaactualizacion"]
    ubicacion = request.POST["ubicacion"]
    notas = request.POST["notas"]

    inventario = TInventario.objects.get(inventarioid=inventarioid)
    inventario.productoid = productoid
    inventario.cantidadinicial = cantidadinicial
    inventario.cantidadactual = cantidadactual
    inventario.fechaactualizacion = fechaactualizacion
    inventario.ubicacion = ubicacion
    inventario.notas = notas

    inventario.save()
    return redirect("inicio_vistaInventarios")

def borrarInventario(request, inventarioid):
    inventario = TInventario.objects.get(inventarioid=inventarioid)
    inventario.delete()
    return redirect("inicio_vistaInventarios")
