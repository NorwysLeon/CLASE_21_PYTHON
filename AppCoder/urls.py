from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/', crearCliente, name="cliente"),
    path('vendedor/', crearVendedor, name="vendedor"),
    path('producto/', crearProducto, name="producto"),
    path('', inicio, name="inicio"),
]
