# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0011_auto_20170130_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='airport_out',
        ),
        migrations.AddField(
            model_name='route',
            name='airport_out',
            field=models.ManyToManyField(to='myfly.Airport', verbose_name='Место вылета'),
        ),
    ]
