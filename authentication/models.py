# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.name

# class CustomUser(AbstractUser):
#     organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True, blank=True, related_name='users')

#     def __str__(self):
#         return self.username