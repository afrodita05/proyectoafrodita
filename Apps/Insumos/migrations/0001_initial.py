# Generated by Django 4.1 on 2022-11-21 22:44

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
                ('nombreInsumo', models.TextField(null=True, verbose_name='Insumo')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('tipoUnidad', models.CharField(max_length=14, null=True)),
            ],
        ),
    ]
