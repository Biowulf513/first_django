# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0012_auto_20170123_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=20, verbose_name='Модель')),
                ('style', models.PositiveSmallIntegerField(choices=[(1, 'Пассажирский'), (2, 'Чартерный'), (3, 'Почтовый'), (4, 'Военный')], max_length=1, verbose_name='Тип')),
                ('seat', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Кол-во мест', max_length=3)),
                ('reg_numb', models.CharField(max_length=6, verbose_name='Рег. номер')),
                ('manufacture', models.DateTimeField(verbose_name='Дата выпуска')),
            ],
            options={
                'verbose_name_plural': 'Модели самолётов',
                'verbose_name': 'Модель самолёта',
            },
        ),
        migrations.CreateModel(
            name='PlaneStock',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('purchase', models.DateTimeField(verbose_name='Дата покупки')),
                ('last_refit', models.DateTimeField(null=True, verbose_name='Последний осмотр', blank=True)),
                ('fly_col', models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Кол-во полётов', max_length=4)),
                ('planModel', models.ForeignKey(to='myfly.PlaneModel')),
            ],
            options={
                'verbose_name_plural': 'Самолёты в ангаре',
                'verbose_name': 'Самолёт в ангаре',
            },
        ),
    ]
