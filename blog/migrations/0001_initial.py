# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('Baslik', models.CharField(max_length=200)),
                ('Yazi', models.TextField()),
                ('Yazilma_Tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('Yayinlama_Tarihi', models.DateTimeField(null=True, blank=True)),
                ('Yazar', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
