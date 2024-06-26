from django.db import models
from django.forms import ValidationError
from django.db import models
from django.db.models import Sum
from django.contrib.auth.hashers import make_password
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
    categoria = models.CharField(max_length=100, default='')
    nomproducto = models.CharField(max_length=100)
    precio = models.FloatField(validators=[validate_positive])
    descrip = models.TextField(default='')
    imagen = models.URLField(default='')
    def __str__(self):
        return self.nomproducto
class cliente(models.Model):
    idc = models.AutoField(primary_key=True)
    correo = models.EmailField(unique = True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.password is not None and self.password != '':
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
class telefono(models.Model):
    numero = models.CharField(max_length=100, primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)    
class direccionentrega(models.Model):
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100, primary_key=True)
class repartidor(models.Model):
    idr = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique = True)
    password = models.CharField(max_length=250, null=True, blank=True)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    activo = models.BooleanField(default=False)
    vehiculo = models.CharField(max_length=100)
    licencia = models.CharField(max_length=100, null=True, blank=True)
    fechavencimiento = models.DateField(null=True, blank=True)
    ocupado = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.password is not None and self.password != '':
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre + ' ' + self.apellido
class colarepartidor(models.Model):
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE)
    n = models.PositiveIntegerField()
    def __str__(self):
        return str(self.idr.nombre)
class carrito(models.Model):
    idcarrito = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(producto, through='carritoproducto')
    comprado = models.BooleanField(default=False)
    comentarios = models.TextField(null=True, blank=True)
class carritoproducto(models.Model):
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ('carrito', 'producto')
class pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    idcarrito = models.ForeignKey(carrito, on_delete=models.CASCADE, null=True, blank=True)
    entregado = models.BooleanField(default=False)
    fechainicio = models.DateTimeField(auto_now_add=True)
    fechafin = models.DateTimeField(null = True, blank = True)
    pickup = models.BooleanField(default=True)
    total = models.FloatField(default=0, null=True, blank=True)
    
class entrega(models.Model):
    idc = models.ForeignKey(cliente, on_delete=models.CASCADE)
    idpedido = models.ForeignKey(pedido, on_delete=models.CASCADE)
    direccion = models.ForeignKey(direccionentrega, on_delete=models.CASCADE)
    idr = models.ForeignKey(repartidor, on_delete=models.CASCADE, null = True, blank = True)
    def __str__(self) -> str:
        return self.idr.nombre
class producto_mas_vendido(models.Model):
    productotendencia = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidadt = models.PositiveIntegerField(default=0)
    def __str__(self) -> str:
        return str(self.productotendencia.nomproducto)
class pedidos_por_dia(models.Model):
    dia = models.DateField(unique=True)
    cantidadp = models.IntegerField(default=0)
class pedidosperiodo(models.Model):
    fechainicio = models.DateField()
    fechafin = models.DateField()
    cantidadp = models.IntegerField(default=0)
    class Meta:
        unique_together = ('fechainicio', 'fechafin')