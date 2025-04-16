from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from core.models import Organization

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