# Generated by Django 4.1 on 2022-11-19 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendacosto',
            name='idCita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Citas.citas'),
        ),
    ]
