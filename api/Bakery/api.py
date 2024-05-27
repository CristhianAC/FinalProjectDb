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
    #http://127.0.0.1:8000/api/api/producto/eliminar/
    @action(detail=False, methods=['delete'])
    def eliminar(self, request):
        idp = request.query_params['idp']
        Prroducto = get_object_or_404(producto, idp=idp)
        Prroducto.delete()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def agregar(self, request):
        categoria = request.query_params['categoria']
        nomproducto = request.query_params['nomproducto']
        precio = request.query_params['precio']
        descrip = request.query_params['descrip']
        imagen = request.query_params['imagen']
        producto = producto.objects.create(categoria=categoria, nomproducto=nomproducto, precio=precio, descrip=descrip, imagen=imagen)
        return Response(status=status.HTTP_200_OK)
class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer  
    @action(detail=True, methods=['post'])
    def agregar_cliente(self, request):
        idc = request.query_params['idc']
        nombre = request.query_params['nombre']
        apellido = request.query_params['apellido']
        contraseña = request.query_params['contraseña']
        admin = request.query_params['admin']
        cliente = cliente.objects.create(idc=idc, nombre=nombre, apellido=apellido, contraseña=contraseña, admin=admin)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_cliente(self, request):
        idc = request.query_params['idc']
        cliente = get_object_or_404(cliente, idc=idc)
        cliente.delete()
        return Response(status=status.HTTP_200_OK)
class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PedidoSerializer
    @action(detail=True, methods=['post'])
    def agregar_pedido(self, request):
        idc = request.query_params['idc']
        estadopedido = request.query_params['estadopedido']
        fecha = request.query_params['fecha']
        cliente = get_object_or_404(cliente, idc=idc)
        pedido = pedido.objects.create(idc=cliente, estadopedido=estadopedido, fecha=fecha)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_pedido(self, request):
        idpedido = request.query_params['idpedido']
        pedido = get_object_or_404(pedido, idpedido=idpedido)
        pedido.delete()
        return Response(status=status.HTTP_200_OK)
class telefonoViewSet(viewsets.ModelViewSet):
    queryset = telefono.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TelefonoSerializer
    @action(detail=True, methods=['post'])
    def agregar_telefono(self, request):
        idc = request.query_params['idc']
        Numero = request.query_params['Numero']
        cliente = get_object_or_404(cliente, idc=idc)
        telefono = telefono.objects.create(idc=cliente, Numero=Numero)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_telefono(self, request):
        Numero = request.query_params['Numero']
        telefono = get_object_or_404(telefono, Numero=Numero)
        telefono.delete()
        return Response(status=status.HTTP_200_OK)
class direccionentregaViewSet(viewsets.ModelViewSet):
    queryset = direccionentrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DireccionEntregaSerializer

    @action(detail=True, methods=['post'])
    def agregar_direccion(self, request):
        idc = request.query_params['idc']
        direccion = request.query_params['direccion']
        cliente = get_object_or_404(cliente, idc=idc)
        direccion = direccionentrega.objects.create(idc=cliente, direccion=direccion)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_direccion(self, request):
        codigodireccion = request.query_params['codigodireccion']
        direccion = get_object_or_404(direccionentrega, codigodireccion=codigodireccion)
        direccion.delete()
        return Response(status=status.HTTP_200_OK)
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

    @action(detail=True, methods=['post'])
    def agregar_repartidor(self, request):
        nombre = request.query_params['nombre']
        apellido = request.query_params['apellido']
        telefono = request.query_params['telefono']
        repartidor = repartidor.objects.create(nombre=nombre, apellido=apellido, telefono=telefono)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_repartidor(self, request):
        idr = request.query_params['idr']
        repartidor = get_object_or_404(repartidor, idr=idr)
        repartidor.delete()
        return Response(status=status.HTTP_200_OK)   
class entregaViewSet(viewsets.ModelViewSet):
    queryset = entrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntregaSerializer
    @action(detail=True, methods=['post'])
    def agregar_entrega(self, request):
        idc = request.query_params['idc']
        idpedido = request.query_params['idpedido']
        direccion = request.query_params['direccion']
        idr = request.query_params['idr']
        idfecha = request.query_params['idfecha']
        cliente = get_object_or_404(cliente, idc=idc)
        pedido = get_object_or_404(pedido, idpedido=idpedido)
        direccion = get_object_or_404(direccionentrega, direccion=direccion)
        repartidor = get_object_or_404(repartidor, idr=idr)
        fecha = get_object_or_404(fecha, idfecha=idfecha)
        entrega = entrega.objects.create(idc=cliente, idpedido=pedido, direccion=direccion, idr=repartidor, fecha=fecha)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_entrega(self, request):
        codigoentrega = request.query_params['codigoentrega']
        entrega = get_object_or_404(entrega, codigoentrega=codigoentrega)
        entrega.delete()
        return Response(status=status.HTTP_200_OK)
class disponibilidadViewSet(viewsets.ModelViewSet):
    queryset = disponibilidad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DisponibilidadSerializer
    @action(detail=True, methods=['post'])
    def agregar_disponibilidad(self, request):
        idr = request.query_params['idr']
        diasdisp = request.query_params['diasdisp']
        horasdisp = request.query_params['horasdisp']
        repartidor = get_object_or_404(repartidor, idr=idr)
        disponibilidad = disponibilidad.objects.create(idr=repartidor, diasdisp=diasdisp, horasdisp=horasdisp)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_disponibilidad(self, request):
        idr = request.query_params['idr']
        disponibilidad = get_object_or_404(disponibilidad, idr=idr)
        disponibilidad.delete()
        return Response(status=status.HTTP_200_OK)
class mediotranspViewSet(viewsets.ModelViewSet):
    queryset = mediotransp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MedioTranspSerializer

    @action(detail=True, methods=['post'])
    def agregar_mediotransp(self, request):
        idr = request.query_params['idr']
        vehiculo = request.query_params['vehiculo']
        fechavenci = request.query_params['fechavenci']
        licencia = request.query_params['licencia']
        repartidor = get_object_or_404(repartidor, idr=idr)
        mediotransp = mediotransp.objects.create(idr=repartidor, vehiculo=vehiculo, fechavenci=fechavenci, licencia=licencia)
        return Response(status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'])
    def eliminar_mediotransp(self, request):
        idr = request.query_params['idr']
        mediotransp = get_object_or_404(mediotransp, idr=idr)
        mediotransp.delete()
        return Response(status=status.HTTP_200_OK)
class colarepartidorViewSet(viewsets.ModelViewSet):
    queryset = colarepartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = colaRepartidorSerializer
    #http://127.0.0.1:8000/api/api/colarepartidor/agregar/agregar/
    @action(detail=True, methods=['post'])
    def agregar(self, request, pk=None):
        repartidor_id = request.query_params['idr']
        try:    
            repar = repartidor.objects.get(idr=repartidor_id)
            cola = colarepartidor.objects.create(idr=repar)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #http://127.0.0.1:8000/api/api/colarepartidor/agregar/eliminar/
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
class carritoViewSet(viewsets.ModelViewSet):
    queryset = carrito.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarritoSerializer
    
    def get_queryset(self):
        return carrito.objects.filter(idc=self.request.user)

    @action(detail=True, methods=['post'])
    def agregar_carrito(self, request):
        idp = request.query_params['idp']
        cantidad = request.query_params['cantidad']
        producto = get_object_or_404(producto, idp=idp)
        carrit, creado = carrito.objects.get_or_create(cliente=request.user.cliente)
        item_carrito, creado = itemcarrito.objects.get_or_create(carrito=carrito, producto=producto)
        if not creado:
            item_carrito.cantidad += cantidad
        else:
            item_carrito.cantidad = cantidad
        item_carrito.save()

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def ver_carrito(self, request):
        carrito = get_object_or_404(carrito, cliente=request.user.cliente)
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data, status=status.HTTP_200_OK)