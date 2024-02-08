from django.db import models

class Cliente(models.Model):
    dni = models.BigIntegerField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    apellido = models.CharField("Apellido", max_length=50)
    direccion = models.CharField("Direccion", max_length=50)
    telefono = models.IntegerField("Telefono")

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.dni}, {self.nombre}, {self.apellido}"

