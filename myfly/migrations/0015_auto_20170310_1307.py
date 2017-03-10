# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0014_auto_20170131_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(blank=True, max_length=4, verbose_name='Международный код', null=True),
        ),
        migrations.AlterField(
            model_name='airport',
            name='international',
            field=models.BooleanField(verbose_name='Интернационален', default=True),
        ),
        migrations.AlterField(
            model_name='plane',
            name='plane_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='myfly.PlaneType', verbose_name='Модель самолёта', null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='plane',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='myfly.Plane', verbose_name='Самолёт', null=True),
        ),
    ]
