# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-13 05:02
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raster_aggregation', '0017_auto_20171124_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='aggregationlayer',
            name='extent',
            field=django.contrib.gis.db.models.fields.PolygonField(null=True, srid=3857),
        ),
    ]
