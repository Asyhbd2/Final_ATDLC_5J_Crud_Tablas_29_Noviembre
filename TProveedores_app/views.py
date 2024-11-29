from django.shortcuts import render, redirect
from .models import TProveedor

# Vista para gestionar proveedores
def inicio_vistaProveedores(request):
    misproveedores = TProveedor.objects.all()
    return render(request, "gestionarProveedores.html", {"misproveedores": misproveedores})

# Registrar proveedor
def registrarProveedor(request):
    proveedorid = request.POST['proveedorid']
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    direccion = request.POST['direccion']
    fecharegistro = request.POST['fecharegistro']
    productosuministro = request.POST['productosuministro']

    TProveedor.objects.create(
        proveedorid=proveedorid,
        nombre=nombre,
        telefono=telefono,
        correo=correo,
        direccion=direccion,
        fecharegistro=fecharegistro,
        productosuministro=productosuministro
    )
    return redirect('inicio_vistaProveedores')

# Editar proveedor
def editarProveedor(request):
    proveedorid = request.POST['proveedorid']
    proveedor = TProveedor.objects.get(proveedorid=proveedorid)
    proveedor.nombre = request.POST['nombre']
    proveedor.telefono = request.POST['telefono']
    proveedor.correo = request.POST['correo']
    proveedor.direccion = request.POST['direccion']
    proveedor.fecharegistro = request.POST['fecharegistro']
    proveedor.productosuministro = request.POST['productosuministro']
    proveedor.save()
    return redirect('inicio_vistaProveedores')

# Seleccionar proveedor para edición
def seleccionarProveedor(request, proveedorid):
    losproveedores = TProveedor.objects.get(proveedorid=proveedorid)
    return render(request, "editarProveedores.html", {"losproveedores": losproveedores})

# Borrar proveedor
def borrarProveedor(request, proveedorid):
    proveedor = TProveedor.objects.get(proveedorid=proveedorid)
    proveedor.delete()
    return redirect('inicio_vistaProveedores')