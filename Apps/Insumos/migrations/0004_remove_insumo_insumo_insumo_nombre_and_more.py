# Generated by Django 4.1 on 2022-09-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insumos', '0003_remove_insumo_numerofactura_remove_insumo_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='insumo',
        ),
        migrations.AddField(
            model_name='insumo',
            name='nombre',
            field=models.TextField(null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='cantidad',
            field=models.CharField(max_length=4, null=True, verbose_name='Cantidad'),
        ),
    ]
