from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Proyecto Laboratorio Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    ordering = ('id',)

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    ordering = ('id',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')
    ordering = ('id',)