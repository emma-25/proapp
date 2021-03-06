# Generated by Django 3.0 on 2020-09-15 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id_negocio', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=25)),
                ('nombre_local', models.CharField(max_length=20)),
                ('nom_responsable', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='visitas',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='visitas',
            name='celular',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Positivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_test', models.DateTimeField(auto_now=True)),
                ('celular', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proapp.Visitas')),
            ],
        ),
    ]
