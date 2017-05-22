# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20151102_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='text_css_color',
            field=models.CharField(blank=True, null=True, max_length=6),
        ),
    ]
