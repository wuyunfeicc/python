# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-27 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userb_user_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userb',
            name='useremail',
            field=models.CharField(default='', max_length=100),
        ),
    ]
