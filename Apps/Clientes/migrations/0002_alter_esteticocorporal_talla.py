# Generated by Django 4.1 on 2022-11-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esteticocorporal',
            name='talla',
            field=models.CharField(max_length=6),
        ),
    ]
