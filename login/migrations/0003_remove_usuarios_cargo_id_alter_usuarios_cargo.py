# Generated by Django 5.0.3 on 2024-04-30 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_cargo_usuarios_usuarios_cargo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='cargo_id',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.cargo_usuarios'),
        ),
    ]
