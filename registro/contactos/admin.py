from django.contrib import admin

from .models import Contacto,Direccion, Medio,Categoria

admin.site.register(Medio)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Direccion)
