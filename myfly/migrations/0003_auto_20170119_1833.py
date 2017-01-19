# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0002_auto_20170119_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planerep',
            old_name='pid',
            new_name='plane',
        ),
    ]
