# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0003_auto_20170119_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planerep',
            name='fly_sum',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='last_fix',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='old',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='plane',
            field=models.ForeignKey(blank=True, to='myfly.Plane'),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='seats_col',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='planerep',
            name='type_plane',
            field=models.SmallIntegerField(choices=[(1, 'Post'), (2, 'Charter fly'), (3, 'Passenger fly'), (4, 'VIP fly')], blank=True),
        ),
    ]
