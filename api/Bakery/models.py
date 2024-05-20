from django.db import models
from django.forms import ValidationError

# Create your models here.
class Producto(models.Model):
    idp = models.CharField(max_length=100, primary_key=True)
    Categoria = models.CharField(max_length=100)
    nomProducto = models.CharField(max_length=100)
    precio = models.FloatField()
    Descrip = models.CharField(max_length=400)
class CaracteristicasPedido(models.Model):
    idp = models.OneToOneField(Producto, on_delete=models.CASCADE)
    IdPedido = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.FloatField()
class Usuario(models.Model):
    idU = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
class Administrador(models.Model):
    idAdmin = models.OneToOneField(Usuario, on_delete=models.CASCADE)
class Cliente(models.Model):
    idC = models.OneToOneField(Usuario, on_delete=models.CASCADE)
class Pedido(models.Model):
    idPedido = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estadoPedido = models.CharField(max_length=100)
    fecha = models.DateField()
class Telefono(models.Model):
    Numero = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
class DireccionEntrega(models.Model):
    codigoDireccion = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)

def validate_day(value):
    if value < 1 or value > 31:
        raise ValidationError(f'{value} no es un día válido. Debe estar entre 1 y 31.')
def validate_month(value):
    if value < 1 or value > 12:
        raise ValidationError(f'{value} no es un mes válido. Debe estar entre 1 y 12.')

class Fecha(models.Model):
    idFecha = models.CharField(max_length=100, primary_key=True)
    dia = models.IntegerField(validators=[validate_day])
    mes = models.IntegerField(validators=[validate_month])
    anio = models.IntegerField()
    hInicio = models.TimeField()
    hFinal = models.TimeField()
class Repartidor(models.Model):
    idr = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
class Entrega(models.Model):
    codigoEntrega = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(DireccionEntrega, on_delete=models.CASCADE)
    idr = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    Fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
class Disponibilidad(models.Model):
    idr = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    diasDisp = models.CharField(max_length=150)
    horasDisp = models.CharField(max_length=150)
class MedioTransp(models.Model):
    idr = models.ForeignKey(Repartidor, on_delete=models.CASCADE)
    vehiculo = models.CharField(max_length=100)
    fechaVenci = models.DateField()
    licencia = models.CharField(max_length=100)