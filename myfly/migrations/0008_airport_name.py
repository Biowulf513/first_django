# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0007_auto_20170130_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Город', default=5),
            preserve_default=False,
        ),
    ]
