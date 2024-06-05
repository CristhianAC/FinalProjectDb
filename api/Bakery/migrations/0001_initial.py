# Generated by Django 5.0.6 on 2024-06-05 17:59

import Bakery.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('idc', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='pedidos_por_dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(unique=True)),
                ('cantidadp', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('idp', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(default='', max_length=100)),
                ('nomproducto', models.CharField(max_length=100)),
                ('precio', models.FloatField(validators=[Bakery.models.validate_positive])),
                ('descrip', models.TextField(default='')),
                ('imagen', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='repartidor',
            fields=[
                ('idr', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('apellido', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=False)),
                ('vehiculo', models.CharField(max_length=100)),
                ('licencia', models.CharField(blank=True, max_length=100, null=True)),
                ('fechavencimiento', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('idcarrito', models.AutoField(primary_key=True, serialize=False)),
                ('comprado', models.BooleanField(default=False)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='direccionentrega',
            fields=[
                ('direccion', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('idpedido', models.AutoField(primary_key=True, serialize=False)),
                ('entregado', models.BooleanField(default=False)),
                ('fechainicio', models.DateTimeField(auto_now_add=True)),
                ('fechafin', models.DateTimeField(blank=True, null=True)),
                ('pickup', models.BooleanField(default=True)),
                ('total', models.FloatField(blank=True, default=0, null=True)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.cliente')),
                ('idcarrito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bakery.carrito')),
            ],
        ),
        migrations.CreateModel(
            name='pedidosperiodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('cantidadp', models.IntegerField(default=0)),
            ],
            options={
                'unique_together': {('fechainicio', 'fechafin')},
            },
        ),
        migrations.CreateModel(
            name='carritoproducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.producto')),
            ],
            options={
                'unique_together': {('carrito', 'producto')},
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='Bakery.carritoproducto', to='Bakery.producto'),
        ),
        migrations.CreateModel(
            name='producto_mas_vendido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadt', models.PositiveIntegerField(default=0)),
                ('productotendencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.producto')),
            ],
        ),
        migrations.CreateModel(
            name='entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.direccionentrega')),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.cliente')),
                ('idpedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.pedido')),
                ('idr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Bakery.repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='colarepartidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.PositiveIntegerField()),
                ('idr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='telefono',
            fields=[
                ('numero', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('idc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bakery.cliente')),
            ],
        ),
    ]
