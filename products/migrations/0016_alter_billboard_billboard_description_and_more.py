# Generated by Django 4.2.2 on 2023-07-22 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_billboard_billboard_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboard',
            name='billboard_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='billboard_for',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='billboard_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
