# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0011_auto_20170123_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planestock',
            name='planModel',
        ),
        migrations.DeleteModel(
            name='PlaneModel',
        ),
        migrations.DeleteModel(
            name='PlaneStock',
        ),
    ]
