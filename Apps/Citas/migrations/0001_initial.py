# Generated by Django 4.1 on 2022-11-21 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
        ('Servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaCosto',
            fields=[
                ('idAgendaCosto', models.AutoField(primary_key=True, serialize=False)),
                ('sesiones', models.CharField(max_length=2)),
                ('costo', models.CharField(max_length=8)),
                ('abono', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('idCita', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCita', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=10)),
                ('idCliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
                ('idServicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Servicios.servicios')),
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
        migrations.AddField(
            model_name='agendacosto',
            name='idCita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Citas.citas'),
        ),
    ]
