from django.shortcuts import render,redirect
from .models import TProducto
# Create your views here.

def inicio_vistaProductos(request):
    losproductos = TProducto.objects.all()
    return render(request,"gestionarProducto.html",{"misproductos":losproductos})

def seleccionarProducto(request,productoid):
    producto = TProducto.objects.get(productoid=productoid)
    return render(request,"editarProducto.html",{"losproductos":producto})

def registrarProducto(request):
    productoid=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["decimalprecio"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["intstock"]
    fechaingreso=request.POST["dateingreso"]

    guardarProducto=TProducto.objects.create(
        productoid=productoid,nombre=nombre,descripcion=descripcion,precio=precio,categoria=categoria,stock=stock,fechaingreso=fechaingreso
    )
    return redirect("inicio_vistaProductos")

def editarProducto(request):
    productoid=request.POST["numid"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["decimalprecio"]
    categoria=request.POST["txtcategoria"]
    stock=request.POST["intstock"]
    fechaingreso=request.POST["dateingreso"]

    Producto=TProducto.objects.get(productoid=productoid)
    Producto.productoid=productoid
    Producto.nombre=nombre
    Producto.descripcion=descripcion
    Producto.precio=precio
    Producto.categoria=categoria
    Producto.stock=stock
    Producto.fechaingreso = fechaingreso

    Producto.save()
    return redirect("inicio_vistaProductos")

def borrarProducto(request,productoid):
    producto=TProducto.objects.get(productoid=productoid)
    producto.delete()
    return redirect("inicio_vistaProductos")