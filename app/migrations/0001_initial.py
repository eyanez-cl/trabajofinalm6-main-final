# Generated by Django 3.1.7 on 2021-02-25 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=200)),
                ('clave', models.CharField(default='123456', max_length=50)),
                ('rut', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('direccion', models.CharField(max_length=150)),
                ('ocupacion', models.CharField(default='influencer', max_length=150)),
                ('telefono', models.CharField(max_length=20)),
                ('foto', models.CharField(default='complete info', max_length=65535)),
                ('resumen', models.TextField(default='complete la info')),
                ('educacion', models.TextField(default='complete la info')),
                ('historial', models.TextField(default='complete la info')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Examenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('observaciones', models.CharField(max_length=250)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pacientes')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
