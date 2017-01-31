# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0010_city_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'страны', 'verbose_name': 'страна'},
        ),
        migrations.AddField(
            model_name='route',
            name='airport_out',
            field=models.ForeignKey(default=5, to='myfly.Airport', verbose_name='Место вылета'),
            preserve_default=False,
        ),
    ]
