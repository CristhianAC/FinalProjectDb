from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('producto', productoViewSet, 'producto')
router.register('cliente', clienteViewSet, 'cliente')
router.register('pedido', pedidoViewSet, 'pedido')
router.register('telefono', telefonoViewSet, 'telefono')
router.register('direccionentrega', direccionentregaViewSet, 'direccionentrega')
router.register('repartidor', repartidorViewSet, 'repartidor')
router.register('entrega', entregaViewSet, 'entrega')
router.register('colarepartidor', colarepartidorViewSet, 'colarepartidor')
router.register('carrito', carritoViewSet, 'carrito')
router.register('carritoproducto', carritoproductoViewSet, 'carritoproducto')
urlpatterns = router.urls
