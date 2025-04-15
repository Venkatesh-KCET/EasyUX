# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='organizations',
        on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='updated_organizations',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Add more fields as needed

    def __str__(self):
        return self.name

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.PROTECT)

    # Set related_name to avoid clash with the default User model
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Change this to a unique related_name
        blank=True
    )

    def __str__(self):
        return self.username