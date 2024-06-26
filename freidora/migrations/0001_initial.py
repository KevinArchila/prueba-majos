# Generated by Django 5.0.3 on 2024-05-05 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0005_cargo_usuarios_usuario_servicio_and_more'),
        ('parametros', '0004_alter_limpieza_puestos_puesto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cambio_aceite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horario', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=6)),
                ('registro_objeto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parametros.registro_objetos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuarios')),
                ('usuario_servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio')),
            ],
        ),
    ]
