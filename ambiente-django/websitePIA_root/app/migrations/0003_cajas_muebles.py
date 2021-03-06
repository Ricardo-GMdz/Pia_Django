# Generated by Django 3.2.3 on 2021-05-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_lockers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=40)),
                ('presentacion', models.CharField(max_length=40)),
                ('capacidad', models.FloatField()),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Muebles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=40)),
                ('precio', models.FloatField()),
            ],
        ),
    ]
