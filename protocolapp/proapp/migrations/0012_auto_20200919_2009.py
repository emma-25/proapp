# Generated by Django 3.1 on 2020-09-19 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0011_auto_20200919_1907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aviso',
            new_name='Alerta',
        ),
        migrations.RenameField(
            model_name='alerta',
            old_name='visitante',
            new_name='positivo',
        ),
    ]
