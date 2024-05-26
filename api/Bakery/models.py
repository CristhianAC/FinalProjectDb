from django.db import models
from django.forms import ValidationError
from django.db import models

def validate_day(value):
    if value < 1 or value > 31:
        raise ValidationError(f'{value} no es un día válido. Debe estar entre 1 y 31.')
def validate_month(value):
    if value < 1 or value > 12:
        raise ValidationError(f'{value} no es un mes válido. Debe estar entre 1 y 12.')
def validate_positive(value):
    if value < 0:
        raise ValidationError(f'{value} no es un valor válido. Debe ser positivo.')

class producto(models.Model):
    idp = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100)
    nomproducto = models.CharField(max_length=100)
    precio = models.FloatField(validators=[validate_positive])
    descrip = models.TextField()
class caracteristicaspedido(models.Model):
    idp = models.OneToOneField(producto, on_delete=models.CASCADE)
    idpedido = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.FloatField()
class cliente(models.Model):
    idc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
class pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    estadopedido = models.CharField(max_length=100)
    fecha = models.DateField()
class telefono(models.Model):
    Numero = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)    
class direccionentrega(models.Model):
    codigodireccion = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
class fecha(models.Model):
    idfecha = models.CharField(max_length=100, primary_key=True)
    dia = models.IntegerField(validators=[validate_day])
    mes = models.IntegerField(validators=[validate_month])
    anio = models.IntegerField()
    hinicio = models.TimeField()
    hfinal = models.TimeField()
class repartidor(models.Model):
    idr = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
class entrega(models.Model):
    codigoentrega = models.AutoField(primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    idpedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    direccion = models.ForeignKey(direccionentrega, on_delete=models.CASCADE)
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE)
    fecha = models.ForeignKey(fecha, on_delete=models.CASCADE)
class disponibilidad(models.Model):
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE)
    diasdisp = models.CharField(max_length=150)
    horasdisp = models.CharField(max_length=150)
class mediotransp(models.Model):
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE)
    vehiculo = models.CharField(max_length=100)
    fechavenci = models.DateField()
    licencia = models.CharField(max_length=100)
class colarepartidor(models.Model):
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE)
    hora = models.TimeField(auto_now_add=True)