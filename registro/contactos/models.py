from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class Medio(models.Model):
    medio = models.CharField(max_length=50)

    def __str__(self):
        return self.medio

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Direccion(models.Model):
    direccion = models.CharField(
        ("Direccion"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.direccion

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    telefono =  PhoneNumberField(null=True, unique=True)
    telefono =  PhoneNumberField(null=True, unique=True)
    direccion = models.ForeignKey(
        'Direccion',on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField("Fecha", null=True, blank=True, help_text="Fecha en que recibio")
    hora = models.TimeField("Hora:Minuto", blank=True, null=True)
    descripcion = models.TextField(help_text="Descripcion sobre el contacto y pedido", blank=True)

    COMPLETADO = 'C'
    PROCESO = 'P'
    ESTADOS = ((COMPLETADO,'Completado'),(PROCESO,'En proceso'))
    estado = models.CharField(max_length=2, choices=ESTADOS, default=PROCESO)

    orden  = models.PositiveIntegerField(help_text="Numero de Orden", blank=True)

    medio = models.ForeignKey('Medio', on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.nombre
