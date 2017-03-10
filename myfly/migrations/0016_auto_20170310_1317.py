# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0015_auto_20170310_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название', unique=True),
        ),
        migrations.AlterField(
            model_name='plane',
            name='reg_numb',
            field=models.CharField(max_length=6, verbose_name='Рег. номер', unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='number',
            field=models.CharField(max_length=6, verbose_name='Номер', unique=True),
        ),
    ]
