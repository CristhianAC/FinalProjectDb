from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
class CaracteristicasPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicasPedido
        fields = '__all__'
        read_only_fields = ['idp', 'IdPedido', 'precio', 'cantidad']
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ['idC']
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ['idPedido', 'idc', 'estadoPedido', 'fecha']
class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = '__all__'
        read_only_fields = ['idc']
class DireccionEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionEntrega
        fields = '__all__'
        read_only_fields = ['codigoDireccion', 'idc']
class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fecha
        fields = '__all__'
        read_only_fields = ['idFecha', 'dia', 'mes', 'anio', 'hInicio', 'hFinal']
class RepartidorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Repartidor
        fields = '__all__'
        read_only_fields = ['idr']
class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'
        read_only_fields = ['codigoEntrega', 'idc', 'idPedido', 'Direccion', 'idr', 'Fecha']
class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'
        read_only_fields = ['idr', 'diasDisp', 'horasDisp']
class MedioTranspSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioTransp
        fields = '__all__'
        read_only_fields = ['idr']
class colaRepartidorSerializer(serializers.ModelSerializer):
    idr = RepartidorSerializer()
    class Meta:
        model = colaRepartidor
        fields = '__all__'
        read_only_fields = ['idr', 'hora']

