from django.shortcuts import render
from .models import Cliente, Vendedor, Producto

# Create your views here.
def crearCliente(request):
    cliente1=Cliente(nombre="Norwys", apellido="León", telefono="+569123456", correo="norwysleon@gamil.com")
    cliente1.save()
    cadena= f"Cliente {cliente1.nombre} {cliente1.apellido} registrado exitosamente"
    return render(request, "AppCoder/clientes.html")

def crearVendedor(request):
    vendedor1=Vendedor(nombre="Mateo", apellido="Marsili", cargo="Vendedor Zona Norte")
    vendedor1.save()
    cadena= f"La venta se asigno correctamente a {vendedor1.nombre} {vendedor1.apellido} y su cargo es: {vendedor1.cargo}"
    return render(request, "AppCoder/vendedores.html")

def crearProducto(request):
    producto1=Producto(nombre="Cámara Fotografica", descripcion="Cámara de alta resolución, con lentes incluidos", precio=500000)
    producto1.save()
    cadena= f"El producto {producto1.nombre} tiene un valor de: {producto1.precio}"
    return render(request, "AppCoder/productos.html")