# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaneRep',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('type_plane', models.CharField(max_length=20)),
                ('seats_col', models.DecimalField(max_digits=3, decimal_places=0)),
                ('old', models.DecimalField(max_digits=2, decimal_places=0)),
                ('fly_sum', models.DecimalField(max_digits=5, decimal_places=0)),
                ('last_fix', models.DateField()),
                ('funcioning', models.BooleanField(default=True)),
                ('pid', models.ForeignKey(to='myfly.Plane')),
            ],
        ),
        migrations.RemoveField(
            model_name='plane_rep',
            name='pid',
        ),
        migrations.DeleteModel(
            name='Plane_rep',
        ),
    ]
