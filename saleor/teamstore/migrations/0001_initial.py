# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-16 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0009_auto_20170206_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, verbose_name='team name')),
                ('team_code', models.CharField(max_length=25, verbose_name='team code')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='userprofile.Address', verbose_name='shipping address')),
            ],
        ),
    ]