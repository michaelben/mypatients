# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypats', '0003_auto_20170608_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='patient',
        ),
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=32, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=2, verbose_name='性别'),
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
