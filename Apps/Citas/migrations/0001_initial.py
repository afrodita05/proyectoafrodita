# Generated by Django 4.1 on 2022-11-05 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaCosto',
            fields=[
                ('idAgendaCosto', models.AutoField(primary_key=True, serialize=False)),
                ('sesiones', models.CharField(max_length=2)),
                ('costo', models.IntegerField()),
                ('abono', models.IntegerField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('idCita', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCita', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=10)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaFecha',
            fields=[
                ('idAgendaFecha', models.AutoField(primary_key=True, serialize=False)),
                ('fechaAgenda', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=9)),
                ('idAgendaCosto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Citas.agendacosto')),
            ],
        ),
    ]
