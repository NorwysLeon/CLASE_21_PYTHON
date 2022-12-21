from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Vendedor, Producto
from AppCoder.forms import ClienteForm, VendedorForm, ProductoForm




# Create your views here.
def crearCliente(request):
    cliente1=Cliente(nombre="Norwys", apellido="León", telefono="+569123456", correo="norwysleon@gamil.com")
    cliente1.save()
    cadena= f"Cliente {cliente1.nombre} {cliente1.apellido} registrado exitosamente"
    return render(request, "AppCoder/cliente.html")

def crearVendedor(request):
    vendedor1=Vendedor(nombre="Mateo", apellido="Marsili", cargo="Vendedor Zona Norte")
    vendedor1.save()
    cadena= f"La venta se asigno correctamente a {vendedor1.nombre} {vendedor1.apellido} y su cargo es: {vendedor1.cargo}"
    return render(request, "AppCoder/vendedor.html")

def crearProducto(request):
    producto1=Producto(nombre="Cámara Fotografica", descripcion="Cámara de alta resolución, con lentes incluidos", precio=500000)
    producto1.save()
    cadena= f"El producto {producto1.nombre} tiene un valor de: {producto1.precio}"
    return render(request, "AppCoder/producto.html")

def inicio(request):
    return render(request, "AppCoder/inicio.html")

"""def clienteFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        telefono=request.POST["telefono"]
        correo=request.POST["correo"]
        cliente=Cliente(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)
        cliente.save()
        return render (request, "AppCoder/inicio.html", {"mensaje": "Cliente guardado correctamente"})
        pass

    return render(request, "AppCoder/clienteFormulario.html")"""

def clienteFormulario(request):
    if request.method=="POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            telefono=informacion["telefono"]
            correo=informacion["correo"]
            cliente= Cliente(nombre=nombre, apellido=apellido, telefono=telefono, correo=correo)
            cliente.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Cliente guardado correctamente"})
        else: 
            return render(request, "AppCoder/clienteFormulario.html", {"form": form, "mensaje": "Información no valida"})

    else:
        formulario= ClienteForm()
        return render (request, "AppCoder/clienteFormulario.html", {"form": formulario})


def vendedorFormulario(request):
    if request.method=="POST":
        form= VendedorForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            cargo=informacion["cargo"]
            vendedor= Vendedor(nombre=nombre, apellido=apellido, cargo=cargo)
            vendedor.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Vendedor guardado correctamente"})
        else: 
            return render(request, "AppCoder/vendedorFormulario.html", {"form": form, "mensaje": "Información no valida"})

    else:
        formulario= VendedorForm()
        return render (request, "AppCoder/vendedorFormulario.html", {"form": formulario})

def productoFormulario(request):
    if request.method=="POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            descripcion=informacion["descripcion"]
            precio=informacion["precio"]
            producto= Producto(nombre=nombre, descripcion=descripcion, precio=precio)
            producto.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Prodcuto comprado correctamente"})
        else: 
            return render(request, "AppCoder/productoFormulario.html", {"form": form, "mensaje": "Información no valida"})

    else:
        formulario= ProductoForm()
        return render (request, "AppCoder/productoFormulario.html", {"form": formulario})


def busquedaNombre(request):
    return render(request, "AppCoder/busquedaNombre.html")


def buscar(request):
    precio= request.GET["precio"]
    if precio !="":
        productos= Producto.objects.filter(precio__icontains=precio)
        return render(request, "AppCoder/resultadosBusqueda.html", {"productos": productos})
    else:
        return render(request, "AppCoder/busquedaNombre.html", {"mensaje": "Ingresar un nombre para buscar"})