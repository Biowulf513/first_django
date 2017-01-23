# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0010_auto_20170123_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planemodel',
            name='manufacture',
            field=models.DateTimeField(verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='planestock',
            name='last_refit',
            field=models.DateTimeField(verbose_name='Последний осмотр', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planestock',
            name='purchase',
            field=models.DateTimeField(verbose_name='Дата покупки'),
        ),
    ]
