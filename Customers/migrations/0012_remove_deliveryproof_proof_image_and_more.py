# Generated by Django 5.0.2 on 2024-03-31 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0011_deliveryproof_proof_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryproof',
            name='proof_image',
        ),
        migrations.RemoveField(
            model_name='parcel',
            name='proof_image',
        ),
    ]
