# Generated by Django 4.1.5 on 2023-12-06 01:12

from django.db import migrations, models
import django.db.models.deletion
import mantenimiento.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicio', '0001_initial'),
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField(help_text='DD/MM/AAAA', verbose_name='Fecha de cita')),
                ('hora_cita', models.TimeField(help_text='HH/MM/SS', max_length=15, verbose_name='Hora de cita')),
                ('contacto', models.CharField(default='', max_length=10, verbose_name='Contacto')),
                ('descripcion_cita', models.CharField(default='', max_length=50, validators=[mantenimiento.models.alphabetic_validator], verbose_name='Descripcion de la cita')),
                ('estado_cita', models.CharField(choices=[('Programada', 'Programada'), ('Pospuesta', 'Pospuesta'), ('Cancelada', 'Cancelada'), ('En proceso', 'Enproceso'), ('Finalizada', 'Finalizada')], default='Programada', max_length=10, verbose_name='Estado')),
                ('nombreservicios', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicio.servicio', verbose_name='Nombre servicio')),
                ('placa', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculo.vehiculo', verbose_name=' Nombre Usuario')),
            ],
            options={
                'verbose_name_plural': 'Citas',
            },
        ),
    ]