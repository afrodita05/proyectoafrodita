# Generated by Django 4.1 on 2022-11-20 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0002_agendacosto_idcita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendacosto',
            name='idCita',
        ),
    ]
