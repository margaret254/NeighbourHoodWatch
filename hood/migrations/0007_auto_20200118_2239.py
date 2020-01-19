# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-18 19:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0006_auto_20200118_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='business',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='post',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]