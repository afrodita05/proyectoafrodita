# Generated by Django 4.1 on 2022-11-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor',
            field=models.CharField(max_length=60),
        ),
    ]