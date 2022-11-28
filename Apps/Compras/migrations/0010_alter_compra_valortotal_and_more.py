# Generated by Django 4.1 on 2022-11-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0009_alter_compra_valortotal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='ValorTotal',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='costoUnidad',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='subTotal',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='total',
            field=models.CharField(max_length=14, null=True),
        ),
    ]