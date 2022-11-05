# Generated by Django 4.1 on 2022-11-05 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=60)),
                ('sexo', models.CharField(blank=True, max_length=9, null=True)),
                ('documento', models.CharField(max_length=10)),
                ('fechaNacimiento', models.CharField(max_length=10)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('estadoCivil', models.CharField(max_length=11)),
                ('numeroHijos', models.CharField(max_length=2)),
                ('fechaActualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EsteticoCorporal',
            fields=[
                ('idCorporal', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('nombreE', models.CharField(max_length=60)),
                ('tensionA', models.CharField(max_length=2)),
                ('digestivo', models.CharField(max_length=2)),
                ('circulacion', models.CharField(max_length=2)),
                ('endrocrino', models.CharField(max_length=2)),
                ('cardiacos', models.CharField(max_length=2)),
                ('otrosP', models.TextField(blank=True, null=True)),
                ('kilos', models.CharField(blank=True, max_length=7, null=True)),
                ('talla', models.CharField(blank=True, max_length=7, null=True)),
                ('altura', models.CharField(blank=True, max_length=7, null=True)),
                ('masaC', models.CharField(blank=True, max_length=7, null=True)),
                ('siluetas', models.CharField(max_length=20)),
                ('cirugias', models.TextField(blank=True, null=True)),
                ('fibrosis', models.TextField(blank=True, null=True)),
                ('costumbresA', models.TextField(blank=True, null=True)),
                ('deportesP', models.TextField(blank=True, null=True)),
                ('modoV', models.CharField(max_length=10)),
                ('fuma', models.CharField(max_length=2)),
                ('alcohol', models.CharField(max_length=2)),
                ('calidadS', models.CharField(max_length=5)),
                ('notasV', models.TextField(blank=True, null=True)),
                ('problemasT', models.TextField(blank=True, null=True)),
                ('abdomen', models.CharField(max_length=2)),
                ('muslos', models.CharField(max_length=2)),
                ('nalgas', models.CharField(max_length=2)),
                ('espalda', models.CharField(max_length=2)),
                ('piernas', models.CharField(max_length=2)),
                ('brazos', models.CharField(max_length=2)),
                ('notasO', models.TextField(blank=True, null=True)),
                ('tratamientosR', models.TextField(blank=True, null=True)),
                ('tratamientosE', models.TextField(blank=True, null=True)),
                ('dermatitis', models.CharField(max_length=2)),
                ('cirugias1', models.CharField(max_length=2)),
                ('cualesC', models.TextField(blank=True, null=True)),
                ('hemofilia', models.CharField(max_length=2)),
                ('embarazo', models.CharField(max_length=2)),
                ('cancer', models.CharField(max_length=2)),
                ('hepatitis', models.CharField(max_length=2)),
                ('diabetes', models.CharField(max_length=2)),
                ('artritis', models.CharField(max_length=2)),
                ('artrosis', models.CharField(max_length=2)),
                ('escoliosis', models.CharField(max_length=2)),
                ('fracturas', models.CharField(max_length=2)),
                ('implantesM', models.CharField(max_length=2)),
                ('hipertencion', models.CharField(max_length=2)),
                ('herniasD', models.CharField(max_length=2)),
                ('dondeHD', models.TextField(blank=True, null=True)),
                ('hiperlordosis', models.CharField(max_length=2)),
                ('hipercifosis', models.CharField(max_length=2)),
                ('problemasC', models.CharField(max_length=2)),
                ('hipotension', models.CharField(max_length=2)),
                ('osteoporosis', models.CharField(max_length=2)),
                ('osteomielitis', models.CharField(max_length=2)),
                ('comedones', models.CharField(max_length=2)),
                ('pustulas', models.CharField(max_length=2)),
                ('brotes', models.CharField(max_length=2)),
                ('quistes', models.CharField(max_length=2)),
                ('nudulos', models.CharField(max_length=2)),
                ('zonasA', models.TextField(blank=True, null=True)),
                ('adiposidadL', models.CharField(max_length=2)),
                ('adiposidadZ', models.CharField(max_length=2)),
                ('adiposidadC', models.CharField(max_length=2)),
                ('cicatricesEL', models.CharField(max_length=2)),
                ('cicatricesEZ', models.CharField(max_length=2)),
                ('cicatricesET', models.CharField(max_length=2)),
                ('flacidezL', models.CharField(max_length=2)),
                ('flacidezZ', models.CharField(max_length=2)),
                ('flacidezC', models.CharField(max_length=2)),
                ('altVascularesL', models.CharField(max_length=2)),
                ('altVascularesZ', models.CharField(max_length=2)),
                ('altVascularesT', models.CharField(max_length=2)),
                ('celulitisL', models.CharField(max_length=2)),
                ('celulitisZ', models.CharField(max_length=2)),
                ('celulitisC', models.CharField(max_length=2)),
                ('temperatura', models.CharField(max_length=8)),
                ('altpigmentariasAR', models.CharField(max_length=2)),
                ('altpigmentariasAL', models.CharField(max_length=2)),
                ('altpigmentariasAP', models.CharField(max_length=2)),
                ('altpigmentariasAMR', models.CharField(max_length=2)),
                ('altpigmentariasALV', models.CharField(max_length=2)),
                ('altpigmentariasAPV', models.CharField(max_length=2)),
                ('sensacionLG', models.CharField(max_length=2)),
                ('sensacionMG', models.CharField(max_length=2)),
                ('sensacionMUG', models.CharField(max_length=2)),
                ('sensacionLF', models.CharField(max_length=2)),
                ('sensacionMF', models.CharField(max_length=2)),
                ('sensacionMUF', models.CharField(max_length=2)),
                ('sensacionPD', models.CharField(max_length=2)),
                ('sensacionPI', models.CharField(max_length=2)),
                ('retieneL', models.CharField(max_length=2)),
                ('varices', models.CharField(max_length=2)),
                ('aranitas', models.CharField(max_length=2)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='EsteticoFacial',
            fields=[
                ('idFacial', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('nombreE', models.CharField(max_length=60)),
                ('tratamientoM', models.CharField(max_length=2)),
                ('cualTM', models.TextField(blank=True, null=True)),
                ('sustitucionH', models.CharField(max_length=2)),
                ('tomaA', models.CharField(max_length=2)),
                ('drogas', models.CharField(max_length=2)),
                ('alimentosP', models.TextField(blank=True, null=True)),
                ('alimentosR', models.TextField(blank=True, null=True)),
                ('fuma', models.CharField(max_length=2)),
                ('tomaL', models.CharField(max_length=2)),
                ('protegeS', models.CharField(max_length=2)),
                ('duermeB', models.CharField(max_length=2)),
                ('menopausia', models.CharField(max_length=2)),
                ('medicamentosOT', models.CharField(max_length=2)),
                ('cualesOT', models.TextField(blank=True, null=True)),
                ('padeceE', models.CharField(max_length=2)),
                ('cancerP', models.CharField(max_length=2)),
                ('asma', models.CharField(max_length=2)),
                ('lupus', models.CharField(max_length=2)),
                ('herpes', models.CharField(max_length=2)),
                ('hepatitis', models.CharField(max_length=2)),
                ('epilepsias', models.CharField(max_length=2)),
                ('dolorC', models.CharField(max_length=2)),
                ('ampollasF', models.CharField(max_length=2)),
                ('tiroides', models.CharField(max_length=2)),
                ('problemasC', models.CharField(max_length=2)),
                ('psicologicos', models.CharField(max_length=2)),
                ('urinarios', models.CharField(max_length=2)),
                ('nasales', models.CharField(max_length=2)),
                ('digestivos', models.CharField(max_length=2)),
                ('alfahidroxiacidos', models.CharField(max_length=2)),
                ('retinA', models.CharField(max_length=2)),
                ('differin', models.CharField(max_length=2)),
                ('accutane', models.CharField(max_length=2)),
                ('motivoC', models.TextField(blank=True, null=True)),
                ('productoCM', models.TextField(blank=True, null=True)),
                ('normal', models.CharField(max_length=2)),
                ('gruesa', models.CharField(max_length=2)),
                ('aspera', models.CharField(max_length=2)),
                ('suave', models.CharField(max_length=2)),
                ('normal1', models.CharField(max_length=2)),
                ('cerrado', models.CharField(max_length=2)),
                ('dilatado', models.CharField(max_length=2)),
                ('zonasM', models.CharField(max_length=2)),
                ('zonasB', models.CharField(max_length=2)),
                ('normal2', models.CharField(max_length=2)),
                ('deshidratada', models.CharField(max_length=2)),
                ('hiperdeshidratada', models.CharField(max_length=2)),
                ('fototipoP', models.CharField(max_length=10)),
                ('lineasF', models.CharField(max_length=2)),
                ('profundas', models.CharField(max_length=2)),
                ('flacidez', models.CharField(max_length=2)),
                ('parpados', models.CharField(max_length=2)),
                ('cuello', models.CharField(max_length=2)),
                ('nasogenianos', models.CharField(max_length=2)),
                ('labios', models.CharField(max_length=2)),
                ('comedones', models.CharField(max_length=2)),
                ('milias', models.CharField(max_length=2)),
                ('quistes', models.CharField(max_length=2)),
                ('melasma', models.CharField(max_length=2)),
                ('hipercromia', models.CharField(max_length=2)),
                ('edema', models.CharField(max_length=2)),
                ('grasa', models.CharField(max_length=2)),
                ('rutinasH', models.TextField(blank=True, null=True)),
                ('cuidadosH', models.TextField(blank=True, null=True)),
                ('mensuales', models.CharField(max_length=2)),
                ('productoH', models.TextField(blank=True, null=True)),
                ('idCliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Clientes.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('idSesiones', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=10)),
                ('Nseciones', models.CharField(max_length=2)),
                ('valor', models.IntegerField()),
                ('abono', models.IntegerField()),
                ('estado', models.CharField(max_length=9)),
                ('fechaActualizacion', models.DateTimeField(auto_now=True)),
                ('idCorporal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Clientes.esteticocorporal')),
                ('idFacial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Clientes.esteticofacial')),
            ],
        ),
        migrations.CreateModel(
            name='ControlMedidas',
            fields=[
                ('idMedidas', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=10)),
                ('brazoD', models.CharField(max_length=7)),
                ('brazoI', models.CharField(max_length=7)),
                ('abdomenA', models.CharField(max_length=7)),
                ('cintura', models.CharField(max_length=7)),
                ('abdomenB', models.CharField(max_length=7)),
                ('piernaD', models.CharField(max_length=7)),
                ('piernaI', models.CharField(max_length=7)),
                ('idCorporal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Clientes.esteticocorporal')),
            ],
        ),
    ]
