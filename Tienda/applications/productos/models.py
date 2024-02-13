from django.db import models
from applications.proveedor.models import Proveedor

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True)
    marca = models.CharField("Marca", max_length=100)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.marca
    

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField("Tipo", max_length=100)
    descripcion = models.CharField("Descripción", max_length=100)
    precio = models.FloatField("Precio")
    cantidad = models.IntegerField("Cantidad",default = 0)
    marca = models.ManyToManyField(Marca)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, default=None)
    
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.precio}"