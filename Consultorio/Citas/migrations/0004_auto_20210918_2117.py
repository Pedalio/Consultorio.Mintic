# Generated by Django 3.2.7 on 2021-09-19 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0003_alter_pacientes_telefono'),
    ]

    operations = [
        migrations.DeleteModel(
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='citas',
            name='horaServicio',
        ),
    ]
