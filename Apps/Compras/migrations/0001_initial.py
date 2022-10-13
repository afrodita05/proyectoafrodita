# Generated by Django 4.1 on 2022-10-13 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Proveedores', '0001_initial'),
        ('Insumos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.AutoField(primary_key=True, serialize=False)),
                ('codigoCompra', models.CharField(max_length=10)),
                ('numeroFactura', models.CharField(max_length=60)),
                ('fechaRecibo', models.DateTimeField(auto_now_add=True)),
                ('ValorTotal', models.CharField(max_length=10)),
                ('idProveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Compra', to='Proveedores.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Compra',
            fields=[
                ('idDetalle_Compra', models.AutoField(primary_key=True, serialize=False)),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Compras.compra')),
                ('idInsumo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Insumos.insumo')),
            ],
        ),
    ]
