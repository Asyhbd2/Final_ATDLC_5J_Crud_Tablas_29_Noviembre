from django.urls import path
from TPedidos_app import views

urlpatterns = [
    path("pedido", views.inicio_vistaPedidos, name="inicio_vistaPedidos"),
    path("registrarPedido/", views.registrarPedido, name="registrarPedido"),
    path("editarPedido/", views.editarPedido, name="editarPedido"),
    path("seleccionarPedido/<pedidoid>", views.seleccionarPedido, name="seleccionarPedido"),
    path("borrarPedido/<pedidoid>", views.borrarPedido, name="borrarPedido")
]