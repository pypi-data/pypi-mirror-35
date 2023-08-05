# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 10:55
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import wagtail.contrib.wagtailroutablepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0024_alter_page_content_type_on_delete_behaviour'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutablePageTest',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
    ]
