from django.db import models

class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    direccion = models.CharField("Direccion", max_length=50)
    telefono = models.IntegerField("Telefono")


    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.id}, {self.nombre}, {self.apellido}"
