# Generated by Django 5.0.2 on 2024-03-21 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], max_length=20)),
                ('receiver_name', models.CharField(max_length=100)),
                ('receiver_address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivered_at', models.DateTimeField(null=True)),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier_parcels', to='Customers.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.user')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryProof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_image', models.ImageField(upload_to='delivery_proofs/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customers.parcel')),
            ],
        ),
    ]
