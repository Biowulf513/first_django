# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('reg_number', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Plane_rep',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type_plane', models.CharField(max_length=20)),
                ('seats_col', models.DecimalField(decimal_places=0, max_digits=3)),
                ('old', models.DecimalField(decimal_places=0, max_digits=2)),
                ('fly_sum', models.DecimalField(decimal_places=0, max_digits=5)),
                ('last_fix', models.DateField()),
                ('funcioning', models.BooleanField(default=True)),
                ('pid', models.ForeignKey(to='myfly.Plane')),
            ],
        ),
    ]
