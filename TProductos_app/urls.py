from django.urls import path
from TProductos_app import views

urlpatterns = [
    path("producto",views.inicio_vistaProductos,name="inicio_vistaProductos"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("seleccionarProducto/<productoid>",views.seleccionarProducto,name="seleccionarProducto"),
    path("borrarProducto/<productoid>",views.borrarProducto,name="borrarProducto")
]
