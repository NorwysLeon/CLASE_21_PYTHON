from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono= models.CharField(max_length=20)
    correo= models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.telefono} - {self.correo}"
 

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    cargo= models.CharField (max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

class Producto(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=200)
    precio= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.descripcion} - {self.precio}"