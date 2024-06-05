from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import carritoproducto, producto_mas_vendido
@receiver(post_save, sender=carritoproducto)
def productos_mas_vendidos(sender,instance,created,**kwargs):
    if created:
        producto = instance.producto
        if producto_mas_vendido.objects.filter(productotendencia = producto).exists():
            producto_mas_vendido.objects.filter(productotendencia = producto).update(cantidadt = producto_mas_vendido.objects.get(productotendencia = producto).cantidadt + instance.cantidad)
        else:
            producto_mas_vendido.objects.create(productotendencia = producto, cantidadt = instance.cantidad)