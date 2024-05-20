from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
class productoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductoSerializer
    @action(detail=False, methods=['delete'])
    def eliminar(self, request):
        idp = request.query_params['idp']
        Prroducto = get_object_or_404(Producto, idp=idp)
        Prroducto.delete()
        return Response(status=status.HTTP_200_OK)
class caracteristicasPedidoViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasPedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CaracteristicasPedidoSerializer

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsuarioSerializer

class administradorViewSet(viewsets.ModelViewSet):  
    queryset = Administrador.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AdministradorSerializer

class clienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer

class pedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PedidoSerializer

class telefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TelefonoSerializer

class direccionEntregaViewSet(viewsets.ModelViewSet):
    queryset = DireccionEntrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DireccionEntregaSerializer

class fechaViewSet(viewsets.ModelViewSet):
    queryset = Fecha.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FechaSerializer

class repartidorViewSet(viewsets.ModelViewSet):
    queryset = Repartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RepartidorSerializer

class entregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntregaSerializer

class disponibilidadViewSet(viewsets.ModelViewSet):
    queryset = Disponibilidad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DisponibilidadSerializer
class medioTranspViewSet(viewsets.ModelViewSet):
    queryset = MedioTransp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MedioTranspSerializer

