from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'
        read_only_fields = ['admin']
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'
class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = telefono
        fields = '__all__'
class DireccionEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = direccionentrega
        fields = '__all__'
        read_only_fields = ['codigodireccion']
class RepartidorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = repartidor
        fields = '__all__'
        read_only_fields = ['idr']
class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = entrega
        fields = '__all__'
class colaRepartidorSerializer(serializers.ModelSerializer):
    idr = RepartidorSerializer()
    class Meta:
        model = colarepartidor
        fields = '__all__'
class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = carritoproducto
        fields = '__all__'
class CarritoSerializer(serializers.ModelSerializer):
    productos = CarritoProductoSerializer(source='carritoproducto_set',many=True, read_only=True)
    class Meta:
        model = carrito
        fields = '__all__'
