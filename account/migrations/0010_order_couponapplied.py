# Generated by Django 4.2.2 on 2023-07-23 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_coupon_maximum_discount'),
        ('account', '0009_cart_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='couponApplied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon'),
        ),
    ]
