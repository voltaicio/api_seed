# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('email', models.EmailField(verbose_name='email address', max_length=128, unique=True)),
                ('is_active', models.BooleanField(verbose_name='is active', default=True)),
                ('is_staff', models.BooleanField(verbose_name='is staff', default=False)),
                ('groups', models.ManyToManyField(related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True)),
                ('user_permissions', models.ManyToManyField(related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
