# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=254)),
                ('create_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
