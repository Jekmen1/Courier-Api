# Generated by Django 5.0.2 on 2024-03-30 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0004_alter_parcel_courier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='sender',
            field=models.ForeignKey(limit_choices_to={'role': 'customers'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
