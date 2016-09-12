# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-12 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0089_auto_20160912_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueModerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.League')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='leaguemoderator',
            unique_together=set([('league', 'player')]),
        ),
    ]
