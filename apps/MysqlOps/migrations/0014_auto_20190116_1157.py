# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-16 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MysqlOps', '0013_auto_20190107_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysqlfastsql',
            name='exec_posi',
            field=models.CharField(blank=True, choices=[('\u4e3b\u5e93', '\u4e3b\u5e93'), ('\u4ece\u5e93', '\u4ece\u5e93'), ('\u96c6\u7fa4', '\u96c6\u7fa4'), ('\u5176\u4ed6', '\u5176\u4ed6')], max_length=30, null=True, verbose_name='\u6267\u884c\u4f4d\u7f6e'),
        ),
        migrations.AlterField(
            model_name='mysqlfastsql',
            name='sql',
            field=models.CharField(max_length=3000, verbose_name=b'sql \xe8\xaf\xad\xe5\x8f\xa5\xe8\xaf\xb7\xe8\x87\xaa\xe5\xb7\xb1\xe9\xaa\x8c\xe8\xaf\x81\xe6\xad\xa3\xe7\xa1\xae'),
        ),
    ]
