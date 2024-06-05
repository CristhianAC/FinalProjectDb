from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
@receiver(post_save, sender=carritoproducto)
def productos_mas_vendidos(sender,instance,created,**kwargs):
    if created:
        producto = instance.producto
        if producto_mas_vendido.objects.filter(productotendencia = producto).exists():
            producto_mas_vendido.objects.filter(productotendencia = producto).update(cantidadt = producto_mas_vendido.objects.get(productotendencia = producto).cantidadt + instance.cantidad)
        else:
            producto_mas_vendido.objects.create(productotendencia = producto, cantidadt = instance.cantidad)

@receiver(post_save, sender=pedido)
def pedidos_por_diaa(sender,instance,created,**kwargs):
    if created:
        fecha = instance.fechainicio.date()
        obj, created = pedidos_por_dia.objects.get_or_create(dia=fecha)
        obj.cantidadp += 1
        obj.save()

@receiver(post_save, sender=pedido)
def pedidos_en_periodo(sender, instance, created, **kwargs):
    if instance.fechafin:  # Asegura que hay una fecha final
        fecha_inicio = instance.fechainicio.date()
        fecha_fin = instance.fechafin.date()
        periodos = pedidosperiodo.objects.filter(fechainicio__lte=fecha_fin, fechafin__gte=fecha_inicio)

        if not periodos.exists():
            pedidosperiodo.objects.create(fechainicio=fecha_inicio, fechafin=fecha_fin, cantidadp=1)
        else:
            for periodo in periodos:
                periodo.cantidadp += 1
                periodo.save()