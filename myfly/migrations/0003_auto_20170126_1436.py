# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0002_auto_20170126_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plane',
            name='planTyepe',
        ),
        migrations.DeleteModel(
            name='Plane',
        ),
        migrations.DeleteModel(
            name='PlaneType',
        ),
    ]
