from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', crearCliente, name="cliente"),
    path('vendedor/', crearVendedor, name="vendedor"),
    path('producto/', crearProducto, name="producto"),
    path('', inicio, name="inicio"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('vendedorFormulario/', vendedorFormulario, name="vendedorFormulario"),
    path('productoFormulario/', productoFormulario, name="productoFormulario"),
    path('busquedaNombre/', busquedaNombre, name="busquedaNombre"),
    path('buscar/', buscar, name="buscar"),


]
