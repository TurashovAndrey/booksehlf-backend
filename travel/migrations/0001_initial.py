# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-26 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0005_auto_20170626_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.DateField()),
                ('book', models.ForeignKey(help_text='Foreign key to book(book id)', on_delete=django.db.models.deletion.CASCADE, related_name='book', to='book.Book')),
            ],
        ),
    ]