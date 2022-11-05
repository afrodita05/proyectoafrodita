# Generated by Django 4.1 on 2022-11-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('configuracion', models.CharField(blank=True, max_length=60, null=True)),
                ('insumos', models.CharField(blank=True, max_length=60, null=True)),
                ('citas', models.CharField(blank=True, max_length=60, null=True)),
                ('clientes', models.CharField(blank=True, max_length=60, null=True)),
                ('servicios', models.CharField(blank=True, max_length=60, null=True)),
                ('compras', models.CharField(blank=True, max_length=60, null=True)),
                ('proveedores', models.CharField(blank=True, max_length=60, null=True)),
                ('usuarios', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
