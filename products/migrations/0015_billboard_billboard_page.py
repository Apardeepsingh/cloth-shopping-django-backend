# Generated by Django 4.2.2 on 2023-07-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_billboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='billboard_page',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('women', 'women'), ('home', 'home')], max_length=255, null=True),
        ),
    ]
