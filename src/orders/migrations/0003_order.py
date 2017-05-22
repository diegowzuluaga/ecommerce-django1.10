# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20151105_1329'),
        ('orders', '0002_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(max_length=120, choices=[('billing', 'Billing'), ('shipping', 'Shipping')], default='created')),
                ('shipping_total_price', models.DecimalField(max_digits=50, decimal_places=2, default=5.99)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('order_id', models.CharField(max_length=20, null=True, blank=True)),
                ('billing_address', models.ForeignKey(related_name='billing_address', null=True, to='orders.UserAddress')),
                ('cart', models.ForeignKey(to='cart.Cart')),
                ('shipping_address', models.ForeignKey(related_name='shipping_address', null=True, to='orders.UserAddress')),
                ('user', models.ForeignKey(to='orders.UserCheckout', null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
