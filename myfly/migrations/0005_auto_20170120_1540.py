# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0004_auto_20170120_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planerep',
            name='plane',
            field=models.ForeignKey(to='myfly.Plane'),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='type_plane',
            field=models.SmallIntegerField(choices=[(1, 'Post'), (2, 'Charter fly'), (3, 'Passenger fly'), (4, 'VIP fly')]),
        ),
    ]
