# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0005_auto_20170126_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('number', models.CharField(max_length=6, verbose_name='Номер')),
                ('time', models.DateTimeField(verbose_name='Время вылета')),
                ('plane', models.ForeignKey(to='myfly.Plane', verbose_name='Самолёт')),
            ],
            options={
                'verbose_name_plural': 'Маршруты',
                'verbose_name': 'Маршрут',
            },
        ),
    ]
