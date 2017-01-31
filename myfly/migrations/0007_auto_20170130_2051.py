# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfly', '0006_airport_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'города',
                'verbose_name': 'город',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Название', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'стрфны',
                'verbose_name': 'стрфна',
            },
        ),
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name_plural': 'аэропорты', 'verbose_name': 'аэропорт'},
        ),
        migrations.AlterModelOptions(
            name='plane',
            options={'verbose_name_plural': 'самолёты в ангаре', 'verbose_name': 'самолёт в ангаре'},
        ),
        migrations.AlterModelOptions(
            name='planetype',
            options={'verbose_name_plural': 'модели самолётов', 'verbose_name': 'модель самолёта'},
        ),
        migrations.AlterModelOptions(
            name='route',
            options={'verbose_name_plural': 'маршруты', 'verbose_name': 'маршрут'},
        ),
        migrations.AddField(
            model_name='airport',
            name='international',
            field=models.BooleanField(default=False, verbose_name='Интернационален'),
        ),
    ]
