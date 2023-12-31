# Generated by Django 4.2.2 on 2023-07-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_bank_options_alter_bank_iban_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='isDelayed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='isOutForPickup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='isReturn',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
