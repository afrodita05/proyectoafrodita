# Generated by Django 4.1 on 2022-10-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('idInsumo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(null=True, verbose_name='Nombre')),
                ('cantidad', models.CharField(max_length=4, null=True, verbose_name='Cantidad')),
            ],
        ),
    ]
