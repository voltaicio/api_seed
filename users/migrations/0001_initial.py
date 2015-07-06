# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('email', models.EmailField(verbose_name='email address', unique=True, max_length=128)),
                ('is_active', models.BooleanField(verbose_name='is active', default=True)),
                ('is_staff', models.BooleanField(verbose_name='is staff', default=False)),
                ('is_superuser', models.BooleanField(verbose_name='is superuser', default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
