# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20151102_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfeatured',
            name='make_image_background',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productfeatured',
            name='image',
            field=models.ImageField(upload_to='image_upload_to_featured'),
        ),
    ]
