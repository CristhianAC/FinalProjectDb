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
class FechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = fecha
        fields = '__all__'
class RepartidorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = repartidor
        fields = '__all__'
        read_only_fields = ['idr']
class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = entrega
        fields = '__all__'
class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = disponibilidad
        fields = '__all__'
class MedioTranspSerializer(serializers.ModelSerializer):
    class Meta:
        model = mediotransp
        fields = '__all__'
class colaRepartidorSerializer(serializers.ModelSerializer):
    idr = RepartidorSerializer()
    class Meta:
        model = colarepartidor
        fields = '__all__'
class itemCarritoSerializer(serializers.ModelSerializer):
    total_precio = serializers.SerializerMethodField()
    class Meta:
        model = itemcarrito
        fields = '__all__'
        read_only_fields = ['idcarrito', 'idproducto']
    def total_precio(self, obj):
        return obj.total_precio()
class CarritoSerializer(serializers.ModelSerializer):
    items = itemCarritoSerializer(many=True, read_only=True)
    total_precio = serializers.SerializerMethodField()
    class Meta:
        model = carrito
        fields = '__all__'
    def get_total_precio(self, obj):
        return sum([item.total_precio() for item in obj.items.all()])
