from django import forms

class ClienteForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    telefono= forms.IntegerField(label="Telefono")
    correo= forms.CharField(label="Correo", max_length=50)

class VendedorForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    cargo= forms.CharField(label="Apellido", max_length=50)