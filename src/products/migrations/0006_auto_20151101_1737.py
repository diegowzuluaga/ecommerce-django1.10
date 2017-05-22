# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20151101_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='activo',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='precio',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nombre',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='activo',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='precio',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='sale_precio',
            new_name='sale_price',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='nombre',
            new_name='title',
        ),
    ]
