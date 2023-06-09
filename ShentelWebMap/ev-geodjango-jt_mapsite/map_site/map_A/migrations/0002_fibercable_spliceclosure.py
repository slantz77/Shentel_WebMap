# Generated by Django 4.1.7 on 2023-05-15 21:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_A', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiberCable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement', models.IntegerField()),
                ('cable_use', models.IntegerField()),
                ('status', models.IntegerField()),
                ('hierarchy', models.IntegerField()),
                ('owner', models.BigIntegerField()),
                ('workorderid', models.CharField(max_length=100, null=True)),
                ('globalid', models.UUIDField()),
                ('cable_type', models.BigIntegerField()),
                ('muuid', models.CharField(max_length=38)),
                ('name', models.CharField(max_length=100, null=True)),
                ('Shape_Length', models.FloatField(null=True)),
                ('Shape', django.contrib.gis.db.models.fields.LineStringField(null=True, srid=4326)),
            ],
            options={
                'db_table': 'fibercable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpliceClosure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closure_make', models.IntegerField()),
                ('closure_size', models.IntegerField()),
                ('closure_use', models.IntegerField(null=True)),
                ('closure_splicecapacity', models.IntegerField(null=True)),
                ('hierarchy', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('status', models.IntegerField()),
                ('owner', models.BigIntegerField()),
                ('globalid', models.UUIDField()),
                ('structureid', models.CharField(max_length=38)),
                ('name', models.CharField(max_length=100, null=True)),
                ('Shape', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
            options={
                'db_table': 'spliceclosure',
                'managed': False,
            },
        ),
    ]
