from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_set",  # Avoid conflict with default user model
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # Avoid conflict with default user model
        blank=True
    )

    def save(self, *args, **kwargs):
        """Ensure password is hashed before saving"""
        if not self.password.startswith('pbkdf2_sha256$'):  # Prevent double hashing
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
