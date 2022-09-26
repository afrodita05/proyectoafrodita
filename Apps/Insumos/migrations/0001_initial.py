# Generated by Django 4.1 on 2022-09-15 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numeroFactura', models.CharField(max_length=5, null=True)),
                ('proveedor', models.TextField(null=True)),
                ('producto', models.TextField(null=True)),
                ('cantidad', models.CharField(max_length=3, null=True)),
                ('valorUnidad', models.CharField(max_length=7)),
            ],
        ),
    ]
