# Generated by Django 4.1.7 on 2023-03-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=255)),
                ('Tipo', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Fecha', models.DateField()),
            ],
        ),
    ]
