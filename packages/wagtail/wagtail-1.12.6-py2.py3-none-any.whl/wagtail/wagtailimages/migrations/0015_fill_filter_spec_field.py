# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 13:25
from __future__ import unicode_literals

from django.db import migrations

from wagtail.wagtailimages.utils import get_fill_filter_spec_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0014_add_filter_spec_field'),
    ]

    forward, reverse = get_fill_filter_spec_migrations('wagtailimages', 'Rendition')
    operations = [
        migrations.RunPython(forward, reverse),
    ]
