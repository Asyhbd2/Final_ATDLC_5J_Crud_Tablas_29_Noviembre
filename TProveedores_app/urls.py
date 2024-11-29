from django.urls import path
from TProveedores_app import views

urlpatterns = [
    path("proveedores", views.inicio_vistaProveedores, name="inicio_vistaProveedores"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("editarProveedor/", views.editarProveedor, name="editarProveedor"),
    path("seleccionarProveedor/<proveedorid>", views.seleccionarProveedor, name="seleccionarProveedor"),
    path("borrarProveedor/<proveedorid>", views.borrarProveedor, name="borrarProveedor"),
]