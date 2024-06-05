from django.contrib import admin
from .models import *

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nomproducto', 'precio']
    search_fields = ['nomproducto']
    list_editable = ['precio']
    list_filter = ['categoria']


admin.site.register(cliente)
@admin.register(pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['idc', 'entregado']
    search_fields = ['idc']
    list_filter = ['entregado']

@admin.register(producto_mas_vendido)
class ProductoMasVendidoAdmin(admin.ModelAdmin):
    list_display = ['productotendencia', 'cantidadt']
    
    ordering = ['-cantidadt']
    
admin.site.register(colarepartidor)

# Register your models here.

