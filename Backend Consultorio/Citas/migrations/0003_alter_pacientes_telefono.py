# Generated by Django 3.2.7 on 2021-09-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0002_alter_medicos_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
    ]
