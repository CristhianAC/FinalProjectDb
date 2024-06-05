from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import viewsets, permissions, status
from .serializers import *
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.contrib.auth.hashers import check_password
from datetime import datetime
from django.db.models import Sum
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
    @action(detail=False, methods=['get'])
    def pedirProducto(self, request):
        idp = request.query_params['idp']
        productoa = get_object_or_404(producto, idp=idp)  # Use the model here, not the serializer
        serializer = ProductoSerializer(productoa)  # Then use the serializer to serialize the model instance
        return Response(serializer.data)
class clienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer  
    @action(detail=False, methods=['post'])
    def agregar_cliente(self, request):
        nombre_completo = request.data.get('nombre')
        if not nombre_completo:
            return Response({'error': 'Nombre completo es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        partes = nombre_completo.split(maxsplit=1)
        nombre = partes[0]
        apellido = partes[1] if len(partes) > 1 else ''
        password = request.data.get('password')
        correo = request.data.get('correo')
        cliente.objects.create(nombre=nombre, apellido=apellido, password=password, admin=False, correo=correo)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
    def eliminar_cliente(self, request):
        idc = request.query_params['idc']
        cliente = get_object_or_404(cliente, idc=idc)
        cliente.delete()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def check_cliente(self, request):
        correo = request.query_params['correo']
        get_object_or_404(cliente, correo=correo)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def check_password(self, request):
        password = request.query_params['password']
        correo = request.query_params['correo']
        clientecheck = cliente.objects.filter(correo=correo).first()
        if clientecheck.password is None:
            return Response('El usuario no tiene registrado una contraseña')
        passwordcompare = check_password(password, clientecheck.password)
        return Response({'nombre': clientecheck.nombre, 'idc': clientecheck.idc, 'correo': clientecheck.correo})
    @action(detail=False, methods=['post'])
    def google_login(self, request):
        correo = request.data.get('correo')
        nombre_completo = request.data.get('nombre')
        if not nombre_completo:
            return Response({'error': 'Nombre completo es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        partes = nombre_completo.split(maxsplit=1)
        nombre = partes[0]
        apellido = partes[1] if len(partes) > 1 else ''
        if not cliente.objects.filter(correo=correo).exists():
            cliente.objects.create(correo=correo, nombre=nombre, apellido=apellido)
            return Response({'Message':'Se ha creado el usuario'},status=status.HTTP_200_OK)
        else:
            return Response({'Message':'El usuario ya existe'})
class pedidoViewSet(viewsets.ModelViewSet):
    queryset = pedido.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PedidoSerializer
    @action(detail=False, methods=['post'])
    def agregar_pedido(self, request):
        correo_cliente = request.data.get('correo')
        numero = request.data.get('numero')
        direccion = request.data.get('direccion')
        pickup = request.data.get('pickup')
        comentario = request.data.get('comentario')
        clientea = get_object_or_404(cliente, correo=correo_cliente)
        numero, created = telefono.objects.get_or_create(idc=clientea, numero=numero)
        direccion, created = direccionentrega.objects.get_or_create(idc=clientea, direccion=direccion)
        carrito_cliente = carrito.objects.filter(cliente=clientea.idc, comprado=False).first()
        carrito_cliente.comentarios = comentario
        carrito_cliente.comprado = True
        if pickup == False:
            pedidoa = pedido.objects.create(idc=clientea, idcarrito=carrito_cliente, pickup = pickup)
            colarepartidora = colarepartidor.objects.first()
            if colarepartidora is None:
                entrega.objects.create(idc=clientea, idpedido = pedidoa, direccion = direccion, idr = None)
            else:
                repartidora = repartidor.objects.filter(idr=colarepartidora.idr.idr).first()
                entrega.objects.create(idc=clientea, idpedido = pedidoa, direccion = direccion, idr = repartidora)
                colarepartidora.delete()
            pedidoa.save()
        else:
            pedidoa = pedido.objects.create(idc=clientea, idcarrito=carrito_cliente)
        serializer = CarritoSerializer(carrito_cliente)
        serializer = serializer.data['productos']
        serializer = [(item['producto'], item['cantidad']) for item in serializer]
        precios = {}
        for producto_id, cantidad in serializer:
            productoa = producto.objects.get(idp=producto_id)
            total = productoa.precio * cantidad
            precios[productoa.nomproducto] = {
            'precio': productoa.precio,
            'cantidad': cantidad,
            'total': total
            }
        pedidoa.total = sum(precios[item]['total'] for item in precios)
        pedidoa.save()
        carrito_cliente.save()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['put'])
    def entregar_pedido(self, request):
        correoa = request.data.get('correo')
        clientea = get_object_or_404(cliente, correo=correoa)
        pedido_cliente = pedido.objects.filter(idc=clientea.idc, entregado=False).first()
        entrega_cliente = entrega.objects.filter(idc=clientea.idc, idpedido=pedido_cliente.idpedido).first()
        repartidor = repartidor.objects.filter(idr=entrega_cliente.idr.idr).first()
        repartidor.ocupado = False
        pedido_cliente.entregado = True
        pedido_cliente.fechafin = datetime.now()
        pedido_cliente.save()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
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
    @action(detail=False, methods=['post'])
    def agregar_telefono(self, request):
        correo = request.data.get('correo')
        numero = request.data.get('numero')
        clientea = get_object_or_404(cliente, correo=correo)
        telefono, created = telefono.objects.get_or_create(idc=cliente, numero=numero)
    @action(detail=False, methods=['delete'])
    def eliminar_telefono(self, request):
        Numero = request.query_params['Numero']
        telefono = get_object_or_404(telefono, Numero=Numero)
        telefono.delete()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def get_telefono(self, request):
        numero = request.query_params['correo']
        clientea = get_object_or_404(cliente, correo=numero)
        telefonos = telefono.objects.filter(idc=clientea.idc)
        serializer = TelefonoSerializer(telefonos, many=True)
        return Response(serializer.data)
class direccionentregaViewSet(viewsets.ModelViewSet):
    queryset = direccionentrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DireccionEntregaSerializer

    @action(detail=False, methods=['post'])
    def agregar_direccion(self, request):
        idc = request.query_params['idc']
        direccion = request.query_params['direccion']
        cliente = get_object_or_404(cliente, idc=idc)
        direccionentrega.objects.create(idc=cliente, direccion=direccion)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
    def eliminar_direccion(self, request):
        codigodireccion = request.query_params['codigodireccion']
        direccion = get_object_or_404(direccionentrega, codigodireccion=codigodireccion)
        direccion.delete()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def get_direcciones(self, request):
        correo = request.query_params['correo']
        clientea = get_object_or_404(cliente, correo=correo)
        direcciones = direccionentrega.objects.filter(idc=clientea.idc)
        serializer = DireccionEntregaSerializer(direcciones, many=True)
        return Response(serializer.data)
class repartidorViewSet(viewsets.ModelViewSet):
    queryset = repartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RepartidorSerializer

    @action(detail=False, methods=['post'])
    def agregar_repartidor(self, request):
        nombre = request.data.get('nombre')
        password = request.data.get('password')
        correo = request.data.get('correo')
        telefono = request.data.get('telefono')
        partes = nombre.split(maxsplit=1)
        nombre = partes[0]
        apellido = partes[1] if len(partes) > 1 else ''
        repartidor.objects.create(nombre=nombre, apellido=apellido, telefono=telefono, password=password, correo=correo)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['put'])
    def activar_repartidor(self, request):
        correo = request.data.get('correo')
        repartidora = get_object_or_404(repartidor, correo=correo)
        if repartidora.ocupado == True:
            return Response({'error': 'El repartidor tiene un pedido activo'}, status=status.HTTP_400_BAD_REQUEST)
        if repartidora.activo:
            repartidora.activo = False
            repartidora.save()
            return Response(status=status.HTTP_200_OK)
        else: 
            repartidora.activo = True
            if entrega.objects.filter(idr = None).exists():
                a = entrega.objects.filter(idr=None).first() 
                repartidora.ocupado = True
                a.idr = repartidora
                repartidor.save()
                a.save()
            else:
                colarepartidor_mayor = colarepartidor.objects.order_by('-n').first()
                if colarepartidor_mayor is None:
                    colarepartidor.objects.create(idr=repartidora, n=1)
                else: 
                    colarepartidor.objects.create(idr=repartidora, n=int(colarepartidor_mayor.n)+1)
                repartidora.save()
            return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def get_pedido(self, request):
        correo = request.query_params['correo']
        repartidora = get_object_or_404(repartidor, correo=correo)
        pedidos = entrega.objects.filter(idr=repartidora, idpedido__entregado=False).first()
        idpedidoa = pedido.objects.filter(idpedido=pedidos.idpedido.idpedido).first()
        carritoa = carrito.objects.filter(idcarrito=idpedidoa.idcarrito.idcarrito).first()
        serializer = CarritoSerializer(carritoa)
        a = serializer.data['productos']
        a = [(item['producto'], item['cantidad']) for item in a]
        precios = {}
        for producto_id, cantidad in a:
            productoa = producto.objects.get(idp=producto_id)
            total = productoa.precio * cantidad
            precios[productoa.nomproducto] = {
            'precio': productoa.precio,
            'cantidad': cantidad,
            'total': total
            }
        return Response({'productos':precios, 'direccion':pedidos.direccion.direccion, 'total':idpedidoa.total})  # Replace 'carritoa' with 'serializer.data['productos']'
    @action(detail=False, methods=['get'])
    def verif_repartidor(self, request):
        correo = request.query_params['correo']
        repartidora = get_object_or_404(repartidor, correo=correo)
        return Response({'activo': repartidora.activo})
class entregaViewSet(viewsets.ModelViewSet):
    queryset = entrega.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EntregaSerializer
    @action(detail=False, methods=['post'])
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
        entrega.objects.create(idc=cliente, idpedido=pedido, direccion=direccion, idr=repartidor, fecha=fecha)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
    def eliminar_entrega(self, request):
        codigoentrega = request.query_params['codigoentrega']
        entrega = get_object_or_404(entrega, codigoentrega=codigoentrega)
        entrega.delete()
        return Response(status=status.HTTP_200_OK) 
class colarepartidorViewSet(viewsets.ModelViewSet):
    queryset = colarepartidor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = colaRepartidorSerializer
    #http://127.0.0.1:8000/api/api/colarepartidor/agregar/agregar/
class carritoViewSet(viewsets.ModelViewSet):
    queryset = carrito.objects.all()
    serializer_class = CarritoSerializer
    lookup_field = 'pk'

    @action(detail=False, methods=['put'])
    def comprar(self, request):
        cliente_correo = request.data.get('correo')
        clientea = get_object_or_404(cliente, correo=cliente_correo)
        carrito_cliente = get_object_or_404(carrito, cliente=clientea.idc, comprado=False)
        carrito_cliente.comprado = True
        carrito_cliente.save()
        return Response(status=status.HTTP_200_OK)
class carritoproductoViewSet(viewsets.ModelViewSet):
    queryset = carritoproducto.objects.all()
    serializer_class = CarritoProductoSerializer
    lookup_field = 'pk'
    def retrieve(self, request, pk=None):
        carrito_producto = self.get_object()
        serializer = self.get_serializer(carrito_producto)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def add_item(self, request):
        cliente_correo = request.data.get('correo')
        clientea = get_object_or_404(cliente, correo=cliente_correo)
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')
            
        carrito_cliente = carrito.objects.filter(cliente=clientea.idc, comprado=False).first()
        if not carrito_cliente:
            carrito_cliente = carrito.objects.create(cliente=clientea)
        productoa = get_object_or_404(producto, idp=producto_id)

        carrito_producto, created = carritoproducto.objects.get_or_create(carrito=carrito_cliente, producto=productoa)
        
        if int(cantidad) > 0:
            carrito_producto.cantidad = int(cantidad)
            carrito_producto.save()
            serializer = CarritoProductoSerializer(carrito_producto)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif int(cantidad) == 0:
            carrito_producto.delete()
            return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['put'])
    def remove_item(self, request):
        cliente_correo = request.data.get('correo')
        clientea = get_object_or_404(cliente, correo=cliente_correo)
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')
        carrito_cliente = carrito.objects.filter(cliente=clientea.idc, comprado=False).first()
        if not carrito_cliente:
            return Response({"error": "No se encontró el carrito del cliente"}, status=status.HTTP_404_NOT_FOUND)
        productoa = get_object_or_404(producto, idp=producto_id)

        try:
            carrito_producto = carritoproducto.objects.get(carrito=carrito_cliente, producto=productoa)
            carrito_producto.cantidad -= int(cantidad)
            if carrito_producto.cantidad <= 0:
                carrito_producto.delete()
            else:
                carrito_producto.save()
            serializer = CarritoProductoSerializer(carrito_producto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except carritoproducto.DoesNotExist:
            return Response({"error": "No se encontró el producto en el carrito"}, status=status.HTTP_404_NOT_FOUND)
    @action(detail=False, methods=['get'])
    def get_cart(self, request):
        cliente_correo = request.query_params.get('correo')
        clientea = get_object_or_404(cliente, correo=cliente_correo)
        carritoa, created = carrito.objects.get_or_create(cliente = clientea, comprado=False)
        serializer = CarritoSerializer(carritoa)
        return Response(serializer.data, status=status.HTTP_200_OK)