# Generated by Django 4.1 on 2022-11-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, default='Afroditalogo.png', null=True, upload_to=''),
        ),
    ]
