# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('purchase', models.DateField(verbose_name='Дата покупки')),
                ('reg_numb', models.CharField(max_length=6, verbose_name='Рег. номер')),
                ('last_refit', models.DateField(verbose_name='Последний осмотр', blank=True, null=True)),
                ('fly_col', models.PositiveSmallIntegerField(verbose_name='Кол-во полётов', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Самолёты в ангаре',
                'verbose_name': 'Самолёт в ангаре',
            },
        ),
        migrations.RenameModel(
            old_name='PlaneModel',
            new_name='PlaneType',
        ),
        migrations.RemoveField(
            model_name='planestock',
            name='planModel',
        ),
        migrations.RenameField(
            model_name='planetype',
            old_name='model',
            new_name='model_name',
        ),
        migrations.DeleteModel(
            name='PlaneStock',
        ),
        migrations.AddField(
            model_name='plane',
            name='planTyepe',
            field=models.ForeignKey(to='myfly.PlaneType', verbose_name='Модель самолёта'),
        ),
    ]
