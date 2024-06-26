# Generated by Django 5.0.3 on 2024-05-03 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_cargo_usuarios_usuario_servicio_and_more'),
        ('parametros', '0002_rename_puesto_id_limpieza_puestos_puesto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='limpieza_puestos',
            name='usuario_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puestos',
            name='usuario_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro_objetos',
            name='usuario_servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='login.usuario_servicio'),
            preserve_default=False,
        ),
    ]
