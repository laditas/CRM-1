# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_salerank'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='openid',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='微信的唯一ID'),
        ),
    ]
