from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'
class CaracteristicasPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = caracteristicaspedido
        fields = '__all__'
        read_only_fields = ['idp', 'idpedido', 'precio', 'cantidad']
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
        read_only_fields = ['idC']
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'
        read_only_fields = ['idPedido', 'idc', 'estadopedido', 'fecha']
class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = telefono
        fields = '__all__'
        read_only_fields = ['idc']
class DireccionEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = direccionentrega
        fields = '__all__'
        read_only_fields = ['codigodireccion', 'idc']
class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = fecha
        fields = '__all__'
        read_only_fields = ['idfecha', 'dia', 'mes', 'anio', 'hinicio', 'hfinal']
class RepartidorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = repartidor
        fields = '__all__'
        read_only_fields = ['idr']
class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = entrega
        fields = '__all__'
        read_only_fields = ['codigoentrega', 'idc', 'idpedido', 'direccion', 'idr', 'fecha']
class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = disponibilidad
        fields = '__all__'
        read_only_fields = ['idr', 'diasDisp', 'horasDisp']
class MedioTranspSerializer(serializers.ModelSerializer):
    class Meta:
        model = mediotransp
        fields = '__all__'
        read_only_fields = ['idr']
class colaRepartidorSerializer(serializers.ModelSerializer):
    idr = RepartidorSerializer()
    class Meta:
        model = colarepartidor
        fields = '__all__'
        read_only_fields = ['idr', 'hora']

