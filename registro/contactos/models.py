from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class Direccion(models.Model):
    direccion = models.CharField(
        ("Direccion"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.city if self.city else ""


class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono =  PhoneNumberField(null=True, unique=True)
    telefono =  PhoneNumberField(null=True, unique=True)
    direccion = models.ForeignKey(
        'Direccion',on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField("Fecha", null=True, blank=True, help_text="Fecha en que recibio")
    hora = models.TimeField(['Hora:Minuto'], blank=True, null=True)
    now = datetime.datetime.now()


    def __str__(self):
        return self.nombre
