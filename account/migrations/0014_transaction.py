# Generated by Django 4.2.2 on 2023-07-26 05:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_order_refundbankdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_id', models.CharField(max_length=100, verbose_name='Payment Id')),
                ('order_id', models.CharField(max_length=100, verbose_name='Order Id')),
                ('signature', models.CharField(max_length=200, verbose_name='Signature')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]