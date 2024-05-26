from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/producto', productoViewSet, 'producto')
router.register('api/caracteristicasPedido', caracteristicasPedidoViewSet, 'caracteristicasPedido')
router.register('api/cliente', clienteViewSet, 'cliente')
router.register('api/pedido', pedidoViewSet, 'pedido')
router.register('api/telefono', telefonoViewSet, 'telefono')
router.register('api/direccionEntrega', direccionEntregaViewSet, 'direccionEntrega')
router.register('api/fecha', fechaViewSet, 'fecha')
router.register('api/repartidor', repartidorViewSet, 'repartidor')
router.register('api/entrega', entregaViewSet, 'entrega')
router.register('api/disponibilidad', disponibilidadViewSet, 'disponibilidad')
router.register('api/medioTransp', medioTranspViewSet, 'medioTransp')
router.register('api/colaRepartidor', colaRepartidorViewSet, 'colaRepartidor')
urlpatterns = router.urls