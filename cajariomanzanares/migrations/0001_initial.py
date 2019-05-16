# Generated by Django 2.2.1 on 2019-05-08 15:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('idRegistroCaja', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Id Registro Caja')),
                ('idVet', models.CharField(max_length=2, verbose_name='Id Veterinario')),
                ('consulta', models.CharField(choices=[('1', 'Consulta1'), ('2', 'Consulta2')], max_length=1, verbose_name='Consulta')),
                ('periodo', models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde')], max_length=1, verbose_name='Periodo')),
                ('fechaCaja', models.DateField(verbose_name='Fecha Caja')),
                ('campoDia', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Caja Dia')),
                ('campoTotal', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Caja Total')),
                ('campoCaja', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Caja')),
                ('impMonedas', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Importe Monedas')),
                ('impBilletes', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Importe Billetes')),
            ],
            options={
                'db_table': 'Caja',
            },
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('idRegistro', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Id Registro')),
                ('idVet', models.CharField(max_length=2, verbose_name='Id Veterinario')),
                ('consulta', models.CharField(choices=[('1', 'Consulta1'), ('2', 'Consulta2')], max_length=1, verbose_name='Consulta')),
                ('fechaRegistro', models.DateField(verbose_name='Fecha Registgro')),
                ('nombreMascota', models.CharField(max_length=30, verbose_name='Nombre Mascota')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre Cliente')),
                ('operacion', models.CharField(max_length=50, verbose_name='Descripción Operación')),
                ('importe', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\?<=>\\d+.\\d+|\\d+$')], verbose_name='Importe')),
                ('metodoPago', models.CharField(choices=[('T', 'Tarjeta'), ('E', 'Efectivo')], max_length=1, verbose_name='Método Pago')),
            ],
            options={
                'db_table': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Veterinarios',
            fields=[
                ('idVet', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Id Veterinario')),
                ('nombreVet', models.CharField(max_length=15, verbose_name='Nombre Veterinario')),
                ('apellidosVet', models.CharField(max_length=30, verbose_name='Apellidos Veterinario')),
            ],
            options={
                'db_table': 'Veterinarios',
            },
        ),
    ]
