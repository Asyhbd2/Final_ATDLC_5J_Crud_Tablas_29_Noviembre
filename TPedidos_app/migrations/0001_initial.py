# Generated by Django 5.1.1 on 2024-11-28 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TClientes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TPedidos',
            fields=[
                ('pedidoid', models.IntegerField(primary_key=True, serialize=False)),
                ('fechapedido', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('estado', models.CharField(max_length=50)),
                ('formpago', models.CharField(max_length=50)),
                ('fechaentrega', models.DateField()),
                ('clienteid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TClientes_app.tcliente')),
            ],
        ),
    ]
