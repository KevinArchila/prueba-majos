# Generated by Django 5.0.3 on 2024-04-29 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=12)),
                ('estado', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=12)),
                ('cargo', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=6)),
            ],
        ),
    ]
