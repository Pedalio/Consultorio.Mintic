# Generated by Django 3.2.7 on 2021-09-29 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaSemana', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionPersonal', models.TextField(blank=True, max_length=500, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('identificacion', models.IntegerField(default=0)),
                ('numTarjetaProfesional', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('edad', models.IntegerField(blank=True, default=1, null=True)),
                ('horariosDisponibles', models.DateTimeField(auto_now_add=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicos.especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='HorasCitasDiarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaDia', models.TimeField()),
                ('diaSemana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicos.diasemana')),
                ('nombreMedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicos.medicos')),
            ],
        ),
    ]
