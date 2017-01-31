# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0012_auto_20170130_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='airport_in',
            field=models.ForeignKey(default=5, verbose_name='Место назначения', to='myfly.Airport', related_name='+'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='route',
            name='airport_out',
        ),
        migrations.AddField(
            model_name='route',
            name='airport_out',
            field=models.ForeignKey(default=5, verbose_name='Место вылета', to='myfly.Airport', related_name='+'),
            preserve_default=False,
        ),
    ]
