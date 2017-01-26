# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0003_auto_20170126_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase', models.DateField(verbose_name='Дата покупки')),
                ('reg_numb', models.CharField(max_length=6, verbose_name='Рег. номер')),
                ('last_refit', models.DateField(blank=True, verbose_name='Последний осмотр', null=True)),
                ('fly_col', models.PositiveSmallIntegerField(blank=True, verbose_name='Кол-во полётов', null=True)),
            ],
            options={
                'verbose_name_plural': 'Самолёты в ангаре',
                'verbose_name': 'Самолёт в ангаре',
            },
        ),
        migrations.CreateModel(
            name='PlaneType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20, verbose_name='Модель')),
                ('style', models.PositiveSmallIntegerField(choices=[(1, 'Пассажирский'), (2, 'Чартерный'), (3, 'Почтовый'), (4, 'Военный')], verbose_name='Тип')),
                ('seat', models.PositiveSmallIntegerField(blank=True, verbose_name='Кол-во мест', null=True)),
                ('manufacture', models.DateField(verbose_name='Дата выпуска')),
            ],
            options={
                'verbose_name_plural': 'Модели самолётов',
                'verbose_name': 'Модель самолёта',
            },
        ),
        migrations.AddField(
            model_name='plane',
            name='planeType',
            field=models.ForeignKey(to='myfly.PlaneType', verbose_name='Модель самолёта'),
        ),
    ]
