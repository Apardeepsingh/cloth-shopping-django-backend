# Generated by Django 4.2.2 on 2023-08-02 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_remove_testimonial_review_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnOrder',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('totalRefundAmount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_order', to='account.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_return_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CancelOrder',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('totalRefundAmount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancel_order', to='account.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_cancel_order', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
