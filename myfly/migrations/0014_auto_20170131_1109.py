# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0013_auto_20170131_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='code',
            field=models.CharField(verbose_name='Международный код', default=5, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='airport_in',
            field=models.ForeignKey(verbose_name='Место назначения', to='myfly.Airport', related_name='incoming_roures'),
        ),
        migrations.AlterField(
            model_name='route',
            name='airport_out',
            field=models.ForeignKey(verbose_name='Место вылета', to='myfly.Airport', related_name='outcoming_roures'),
        ),
    ]
