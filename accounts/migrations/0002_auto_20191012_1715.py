# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-12 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='denzel.jpeg', upload_to='profile_pics'),
        ),
    ]
