# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_productfeatured_text_css_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfeatured',
            old_name='text_rigth',
            new_name='text_right',
        ),
    ]
