# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-27 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0005_auto_20180203_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('package', models.CharField(max_length=10)),
                ('new_subscribe', models.BooleanField()),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_apply', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
