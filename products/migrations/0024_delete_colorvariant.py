# Generated by Django 4.2.2 on 2023-08-03 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_productcolor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ColorVariant',
        ),
    ]