# Generated by Django 4.1 on 2022-09-29 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Configuracion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rol',
            old_name='nombreRol',
            new_name='nombre',
        ),
    ]