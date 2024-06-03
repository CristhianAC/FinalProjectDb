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
        password = request.data.get('password')
        correo = request.data.get('correo')
        clientecheck = cliente.objects.filter(correo=correo).first()
        if clientecheck.password is None:
            return Response('El usuario no tiene registrado una contraseña')
        passwordcompare = check_password(password, clientecheck.password)
        return Response('Contraseña correcta' if passwordcompare else 'Contraseña incorrecta')
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
        idc = request.query_params['idc']
        estadopedido = request.query_params['estadopedido']
        fecha = request.query_params['fecha']
        idcarrito = request.query_params['idcarrito']
        cliente = get_object_or_404(cliente, idc=idc)
        pedido.objects.create(idc=cliente, estadopedido=estadopedido, fecha=fecha, idcarrito=idcarrito)
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
        idc = request.query_params['idc']
        numero = request.query_params['numero']
        cliente = get_object_or_404(cliente, idc=idc)
        telefono.objects.create(idc=cliente, Numero=numero)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
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

    @action(detail=False, methods=['post'])
    def agregar_repartidor(self, request):
        nombre = request.query_params['nombre']
        apellido = request.query_params['apellido']
        telefono = request.query_params['telefono']
        repartidor.objects.create(nombre=nombre, apellido=apellido, telefono=telefono)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
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
    
    @action(detail=False, methods=['get'])
    def pedidos_por_dia(self, request):
        fecha = request.query_params['fecha']
        if not fecha:
            return Response({"error": "Se requiere un parámetro de 'fecha'"}, status=400)        
        queryset = pedido.objects.filter(fecha=fecha).annotate(dia=TruncDay('fecha')).values('dia').annotate(total_pedidos=Count('idpedido'))
        return Response(queryset)
    @action(detail=False, methods=['get'])
    def pedidos_en_periodo(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Se requieren los parámetros 'fecha_inicio' y 'fecha_fin'"}, status=400)

        try:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Formato de fecha inválido. Use 'YYYY-MM-DD'."}, status=400)

        total_pedidos = pedido.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).count()
    @action(detail=False, methods=['get'])
    def pedidos_por_producto(self, request):
        # Filtrar productos solo de pedidos que han sido entregados
        productos_pedidos = carritoproducto.objects.filter(carrito__pedido__estadopedido='entregado')\
            .values('producto__nomproducto')\
            .annotate(total_cantidad=Sum('cantidad'))\
            .order_by('producto__nomproducto')
        return Response(productos_pedidos)
    
class disponibilidadViewSet(viewsets.ModelViewSet):
    queryset = disponibilidad.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DisponibilidadSerializer
    @action(detail=False, methods=['post'])
    def agregar_disponibilidad(self, request):
        idr = request.query_params['idr']
        diasdisp = request.query_params['diasdisp']
        horasdisp = request.query_params['horasdisp']
        repartidor = get_object_or_404(repartidor, idr=idr)
        disponibilidad.objects.create(idr=repartidor, diasdisp=diasdisp, horasdisp=horasdisp)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
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

    @action(detail=False, methods=['post'])
    def agregar_mediotransp(self, request):
        idr = request.query_params['idr']
        vehiculo = request.query_params['vehiculo']
        fechavenci = request.query_params['fechavenci']
        licencia = request.query_params['licencia']
        repartidor = get_object_or_404(repartidor, idr=idr)
        mediotransp.objects.create(idr=repartidor, vehiculo=vehiculo, fechavenci=fechavenci, licencia=licencia)
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=['delete'])
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
    @action(detail=False, methods=['post'])
    def agregar(self, request, pk=None):
        repartidor_id = request.query_params['idr']
        try:    
            repar = repartidor.objects.get(idr=repartidor_id)
            cola = colarepartidor.objects.create(idr=repar)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    #http://127.0.0.1:8000/api/api/colarepartidor/agregar/eliminar/
    @action(detail=False, methods=['delete'])
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
        #cambiar params a get
        cliente_correo = request.data.get('correo')
        clientea = get_object_or_404(cliente, correo=cliente_correo)
        producto_id = request.data.get('producto_id')
        cantidad = request.data.get('cantidad')
        carrito_cliente = carrito.objects.filter(cliente=clientea.idc, comprado=False).first()
        if not carrito_cliente:
            carrito_cliente = carrito.objects.create(cliente=clientea)
        productoa = get_object_or_404(producto, idp=producto_id)

        carrito_producto, created = carritoproducto.objects.get_or_create(carrito=carrito_cliente, producto=productoa)
        carrito_producto.cantidad = int(cantidad)

        carrito_producto.save()
        serializer = CarritoProductoSerializer(carrito_producto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
        