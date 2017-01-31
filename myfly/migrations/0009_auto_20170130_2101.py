# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0008_airport_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(verbose_name='Город', to='myfly.City', default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=20),
        ),
    ]
