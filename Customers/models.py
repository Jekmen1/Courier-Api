from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(AbstractUser):
    CUSTOMER = 'customer'
    COURIER = 'courier'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (COURIER, 'Courier'),
        (ADMIN, 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions_set',
        related_query_name='user',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups_set',
        related_query_name='user',
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Parcel(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'customer'})
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    courier = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='courier_parcels', null=True, limit_choices_to={'role': 'courier'})
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True)
    def __str__(self):
        return self.title

class DeliveryProof(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Parcel.STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=Parcel)
    def create_delivery_proof(sender, instance, created, **kwargs):
        if created:
            DeliveryProof.objects.create(parcel=instance, status=instance.status)

    def __str__(self):
        return f"{self.parcel.title}"