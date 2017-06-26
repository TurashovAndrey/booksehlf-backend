# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-26 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('death_date', models.DateField(null=True)),
            ],
        ),
    ]