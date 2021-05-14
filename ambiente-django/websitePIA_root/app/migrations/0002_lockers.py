# Generated by Django 3.2.3 on 2021-05-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lockers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=40)),
                ('presentacion', models.CharField(max_length=30)),
                ('largo', models.FloatField()),
                ('precio', models.FloatField()),
            ],
        ),
    ]
