# Generated by Django 3.1 on 2020-09-19 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0010_auto_20200919_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitas',
            name='fecha_visita',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
