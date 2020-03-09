from django.contrib import admin

from .models import Contacto,Direccion, Medio,Categoria

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido","celular",'fecha')
    list_filter = ("nombre","apellido","fecha","estado",)
    search_fields = ('nombre','apellido','orden',)
    fields = [('nombre','apellido'),
                ('telefono','celular'),
                ('direccion','fecha','hora'),
                ('descripcion'),
                ('estado','orden'),
                ('medio','categoria'),
                ('email')]


admin.site.register(Medio)
admin.site.register(Categoria)
admin.site.register(Direccion)
