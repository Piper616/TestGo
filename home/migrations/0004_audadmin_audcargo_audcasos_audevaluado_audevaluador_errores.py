# Generated by Django 3.2.7 on 2021-11-03 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20211022_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudAdmin',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'aud_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AudCargo',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'aud_cargo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AudCasos',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'aud_casos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AudEvaluado',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'aud_evaluado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AudEvaluador',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('accion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'aud_evaluador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Errores',
            fields=[
                ('id_error', models.FloatField(primary_key=True, serialize=False)),
                ('codigo_error', models.CharField(blank=True, max_length=20, null=True)),
                ('descripcion_error', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'errores',
                'managed': False,
            },
        ),
    ]
