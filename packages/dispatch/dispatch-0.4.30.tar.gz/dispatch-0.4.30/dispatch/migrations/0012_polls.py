# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0011_article_featured_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('question', models.CharField(max_length=255)),
                ('is_open', models.BooleanField(default=True)),
                ('show_results', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='dispatch.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='PollVote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='dispatch.PollAnswer')),
            ],
        ),
    ]
