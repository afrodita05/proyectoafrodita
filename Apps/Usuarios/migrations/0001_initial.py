# Generated by Django 4.1 on 2022-09-16 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('idPrueba', models.AutoField(primary_key=True, serialize=False)),
                ('at1', models.CharField(max_length=11)),
                ('at2', models.CharField(max_length=11)),
                ('at3', models.CharField(max_length=11)),
            ],
        ),
    ]
