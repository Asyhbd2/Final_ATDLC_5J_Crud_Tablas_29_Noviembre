# Generated by Django 5.1.1 on 2024-11-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TClientes_app', '0001_initial'),
        ('TPedidos_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TPedidos',
            new_name='TPedido',
        ),
    ]