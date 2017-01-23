# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaneModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('model', models.CharField(verbose_name='Модель', max_length=20)),
                ('style', models.PositiveSmallIntegerField(verbose_name='Тип', choices=[(1, 'Пассажирский'), (2, 'Чартерный'), (3, 'Почтовый'), (4, 'Военный')])),
                ('seat', models.PositiveSmallIntegerField(verbose_name='Кол-во мест', blank=True, null=True)),
                ('manufacture', models.DateField(verbose_name='Дата выпуска')),
            ],
            options={
                'verbose_name': 'Модель самолёта',
                'verbose_name_plural': 'Модели самолётов',
            },
        ),
        migrations.CreateModel(
            name='PlaneStock',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('purchase', models.DateField(verbose_name='Дата покупки')),
                ('reg_numb', models.CharField(verbose_name='Рег. номер', max_length=6)),
                ('last_refit', models.DateField(verbose_name='Последний осмотр', blank=True, null=True)),
                ('fly_col', models.PositiveSmallIntegerField(verbose_name='Кол-во полётов', blank=True, null=True)),
                ('planModel', models.ForeignKey(to='myfly.PlaneModel')),
            ],
            options={
                'verbose_name': 'Самолёт в ангаре',
                'verbose_name_plural': 'Самолёты в ангаре',
            },
        ),
    ]
