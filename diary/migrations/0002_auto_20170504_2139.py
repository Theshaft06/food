# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.CharField(default='breakfast', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='diary.User'),
        ),
    ]