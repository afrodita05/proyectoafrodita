# Generated by Django 4.1 on 2022-11-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0005_detalle_compra_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='ValorTotal',
            field=models.FloatField(null=True),
        ),
    ]
