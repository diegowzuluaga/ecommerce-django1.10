# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_percentage',
            field=models.DecimalField(max_digits=10, default=0.085, decimal_places=5),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(max_digits=50, default=25.0, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(max_digits=50, default=25.0, decimal_places=2),
        ),
    ]
