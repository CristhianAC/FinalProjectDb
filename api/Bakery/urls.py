from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/producto', productoViewSet, 'producto')
router.register('api/caracteristicaspedido', caracteristicaspedidoViewSet, 'caracteristicaspedido')
router.register('api/cliente', clienteViewSet, 'cliente')
router.register('api/pedido', pedidoViewSet, 'pedido')
router.register('api/telefono', telefonoViewSet, 'telefono')
router.register('api/direccionentrega', direccionentregaViewSet, 'direccionentrega')
router.register('api/fecha', fechaViewSet, 'fecha')
router.register('api/repartidor', repartidorViewSet, 'repartidor')
router.register('api/entrega', entregaViewSet, 'entrega')
router.register('api/disponibilidad', disponibilidadViewSet, 'disponibilidad')
router.register('api/mediotransp', mediotranspViewSet, 'mediotransp')
router.register('api/colarepartidor', colarepartidorViewSet, 'colarepartidor')
urlpatterns = router.urls