# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-09-15 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20190915_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(db_column='jiaqian', decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
