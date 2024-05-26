from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductoSerializer
    @action(detail=False, methods=['delete'])
    def eliminar(self, request):
        idp = request.query_params['idp']
        Prroducto = get_object_or_404(producto, idp=idp)
        Prroducto.delete()
        return Response(status=status.HTTP_200_OK)
class caracteristicaspedidoViewSet(viewsets.ModelViewSet):
    queryset = caracteristicaspedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CaracteristicasPedidoSerializer
class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer
class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PedidoSerializer
class telefonoViewSet(viewsets.ModelViewSet):
    queryset = telefono.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TelefonoSerializer
class direccionentregaViewSet(viewsets.ModelViewSet):
    queryset = direccionentrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DireccionEntregaSerializer
class fechaViewSet(viewsets.ModelViewSet):
    queryset = fecha.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FechaSerializer
class repartidorViewSet(viewsets.ModelViewSet):
    queryset = repartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RepartidorSerializer
class entregaViewSet(viewsets.ModelViewSet):
    queryset = entrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntregaSerializer
class disponibilidadViewSet(viewsets.ModelViewSet):
    queryset = disponibilidad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DisponibilidadSerializer
class mediotranspViewSet(viewsets.ModelViewSet):
    queryset = mediotransp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MedioTranspSerializer
class colarepartidorViewSet(viewsets.ModelViewSet):
    queryset = colarepartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = colaRepartidorSerializer
    @action(detail=True, methods=['post'])
    def agregar(self, request, pk=None):
        repartidor_id = request.query_params['idr']
        try:    
            repar = repartidor.objects.get(idr=repartidor_id)
            cola = colarepartidor.objects.create(idr=repar)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['delete'])
    def eliminar(self, request, pk=None):
        idr = request.query_params['idr']
        try:
            repar = repartidor.objects.get(idr=idr)
            cola = colarepartidor.objects.get(idr=repar)
            cola.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)