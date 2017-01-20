# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0007_auto_20170120_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planerep',
            name='seats_col',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
