# Generated by Django 5.1.1 on 2024-11-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TProductos',
            fields=[
                ('productoid', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categoria', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('fechaingreso', models.DateField()),
            ],
        ),
    ]
