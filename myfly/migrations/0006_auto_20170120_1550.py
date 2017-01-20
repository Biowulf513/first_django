# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0005_auto_20170120_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planerep',
            name='fly_sum',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='last_fix',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='old',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='seats_col',
            field=models.IntegerField(),
        ),
    ]
