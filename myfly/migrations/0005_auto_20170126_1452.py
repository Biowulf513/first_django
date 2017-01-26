# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0004_auto_20170126_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plane',
            old_name='planeType',
            new_name='plane_type',
        ),
        migrations.RenameField(
            model_name='planetype',
            old_name='model_name',
            new_name='name',
        ),
    ]
