from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    telefono= forms.IntegerField(label="Telefono")
    correo= forms.CharField(label="Correo", max_length=50)

class VendedorForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    cargo= forms.CharField(label="Cargo", max_length=50)


class ProductoForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    descripcion= forms.CharField(label="Descripción", max_length=1000)
    precio= forms.CharField(label="Precio", max_length=20)