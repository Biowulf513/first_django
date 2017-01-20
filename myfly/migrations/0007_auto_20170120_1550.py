# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0006_auto_20170120_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planerep',
            name='last_fix',
            field=models.DateField(null=True, blank=True),
        ),
    ]
