# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-25 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee_django_course', '0042_section_auto_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='auto_pass',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u81ea\u52a8\u901a\u8fc7'),
        ),
    ]
