# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0009_auto_20170120_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaneModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('model', models.CharField(verbose_name='Модель', max_length=20)),
                ('style', models.PositiveSmallIntegerField(verbose_name='Тип', choices=[(1, 'Пассажирский'), (2, 'Чартерный'), (3, 'Почтовый'), (4, 'Военный')], max_length=1)),
                ('seat', models.PositiveSmallIntegerField(null=True, verbose_name='Кол-во мест', blank=True, max_length=3)),
                ('reg_numb', models.CharField(verbose_name='Рег. номер', max_length=6)),
                ('manufacture', models.TimeField(verbose_name='Дата выпуска')),
            ],
            options={
                'verbose_name_plural': 'Модели самолётов',
                'verbose_name': 'Модель самолёта',
            },
        ),
        migrations.CreateModel(
            name='PlaneStock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('purchase', models.TimeField(verbose_name='Дата покупки')),
                ('last_refit', models.TimeField(null=True, verbose_name='Последний осмотр', blank=True)),
                ('fly_col', models.PositiveSmallIntegerField(null=True, verbose_name='Кол-во полётов', blank=True, max_length=4)),
                ('planModel', models.ForeignKey(to='myfly.PlaneModel')),
            ],
            options={
                'verbose_name_plural': 'Самолёты в ангаре',
                'verbose_name': 'Самолёт в ангаре',
            },
        ),
        migrations.RemoveField(
            model_name='planerep',
            name='plane',
        ),
        migrations.DeleteModel(
            name='Plane',
        ),
        migrations.DeleteModel(
            name='PlaneRep',
        ),
    ]
