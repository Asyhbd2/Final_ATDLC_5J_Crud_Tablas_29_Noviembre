from django.urls import path
from TInventario_app import views

urlpatterns = [
    path("inventario", views.inicio_vistaInventarios, name="inicio_vistaInventarios"),
    path("registrarInventario/", views.registrarInventario, name="registrarInventario"),
    path("editarInventario/", views.editarInventario, name="editarInventario"),
    path("seleccionarInventario/<inventarioid>", views.seleccionarInventario, name="seleccionarInventario"),
    path("borrarInventario/<inventarioid>", views.borrarInventario, name="borrarInventario")
]